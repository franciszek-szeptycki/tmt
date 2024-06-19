#!/bin/bash

python manage.py migrate

python manage.py create_user --noinput

gunicorn config.wsgi
