#!/bin/bash

python manage.py migrate --no-input

celery -A registrafirma beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler &

celery -A registrafirma worker -l info &

exec "$@"
