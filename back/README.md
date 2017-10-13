# API Contest

## Quick Start

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py loaddata schedule/fixtures/time_slots.json
python manage.py populate_talks
```

## Routes:

* http://localhost:8000/admin/
* http://localhost:8000/graphql

## Run tests

pytest
