from urllib.parse import urlencode
import json
import pytest
from .models import Speaker, TimeSlot, Talk


def url_string(string='/graphql', **url_params):
    if url_params:
        string += '?' + urlencode(url_params)
    return string


def response_json(response):
    return json.loads(response.content.decode())


# Fixtures

@pytest.fixture
def speaker():
    speaker = Speaker(name='John Doe')
    speaker.save()
    return speaker


@pytest.fixture
def time_slot1():
    ts = TimeSlot(date='2017-11-04', start='11:00', end='11:15')
    ts.save()
    return ts


@pytest.fixture
def time_slot2():
    ts = TimeSlot(date='2017-11-03', start='08:00', end='09:00')
    ts.save()
    return ts


@pytest.fixture
def talk(speaker, time_slot1):
    talk = Talk(name='Lean UX', speaker=speaker, time_slot=time_slot1, room='dos',
                category='UX')
    talk.save()
    return talk


# Tests

@pytest.mark.django_db()
def test_save_speaker(speaker):
    assert Speaker.objects.count() == 1


def test_admin_need_login(client):
    response = client.get('/admin/NW6/4l9Q/')
    assert response.status_code == 302


def test_admin_works(admin_client):
    response = admin_client.get('/admin/NW6/4l9Q/')
    assert response.status_code == 200


def test_graphql_works(client):
    response = client.get(url_string(), HTTP_ACCEPT='text/html')
    assert response.status_code == 200


@pytest.mark.django_db()
def test_graphql_empty_list(client):
    response = client.get(url_string(query='{ allTalks { id } }'))

    assert response.status_code == 200
    assert response_json(response) == {'data': {'allTalks': []}}


@pytest.mark.django_db()
def test_graphql_not_found_returns_null(client):
    response = client.get(url_string(query='{ speaker(id: 234) { id } }'))

    assert response.status_code == 200
    assert response_json(response) == {'data': {'speaker': None}}


@pytest.mark.django_db()
def test_graphql_list_speakers(client, speaker):
    response = client.get(url_string(query='{ allSpeakers { name } }'))

    assert response.status_code == 200
    assert response_json(response) == {'data': {'allSpeakers': [{'name': 'John Doe'}]}}


@pytest.mark.django_db()
def test_graphql_find_speaker(client, speaker):
    response = client.get(url_string(query='{ speaker(id: %d) { name } }' % speaker.id))

    assert response.status_code == 200
    assert response_json(response) == {'data': {'speaker': {'name': 'John Doe'}}}


@pytest.mark.django_db()
def test_graphql_list_time_slots(client, time_slot1, time_slot2):
    response = client.get(url_string(query='{ allTimeSlots { date start end } }'))

    assert response.status_code == 200
    assert response_json(response) == {
        'data': {
            'allTimeSlots': [
                {'date': '2017-11-03', 'start': '08:00:00', 'end': '09:00:00'},
                {'date': '2017-11-04', 'start': '11:00:00', 'end': '11:15:00'},
            ]
        }
    }


@pytest.mark.django_db()
def test_graphql_find_time_slot(client, time_slot1, time_slot2):
    tid = time_slot1.id
    response = client.get(url_string(query='{ timeSlot(id: %d) { start } }' % tid))

    assert response.status_code == 200
    assert response_json(response) == {
        'data': {
            'timeSlot': {'start': '11:00:00'},
        }
    }


@pytest.mark.django_db()
def test_graphql_list_talks(client, talk):
    response = client.get(url_string(query='''
        {
            allTalks {
                name
                room
                category
                isPlaceholder
                timeSlot {
                    start
                }
                speaker {
                    name
                }
            }
        }'''))

    assert response.status_code == 200
    assert response_json(response) == {
        'data': {
            'allTalks': [{
                'name': 'Lean UX',
                'room': 'DOS',
                'category': 'UX',
                'isPlaceholder': False,
                'timeSlot': {'start': '11:00:00'},
                'speaker': {'name': 'John Doe'}
            }],
        }
    }


@pytest.mark.django_db()
def test_graphql_find_talk(client, talk):
    response = client.get(url_string(query='''
        {
            talk(id: %d) {
                name
                room
                category
                isPlaceholder
                timeSlot {
                    start
                }
                speaker {
                    name
                }
            }
        }''' % talk.id))

    assert response.status_code == 200
    assert response_json(response) == {
        'data': {
            'talk': {
                'name': 'Lean UX',
                'room': 'DOS',
                'category': 'UX',
                'isPlaceholder': False,
                'timeSlot': {'start': '11:00:00'},
                'speaker': {'name': 'John Doe'}
            },
        }
    }
