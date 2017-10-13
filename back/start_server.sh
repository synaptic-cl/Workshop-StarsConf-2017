#!/usr/bin/env bash
python manage.py migrate
# python manage.py createsuperuser
python manage.py loaddata schedule/fixtures/time_slots.json
python manage.py populate_talks
python -u manage.py runserver 0.0.0.0:8000