#!/bin/bash

python manage.py db init

# Drop existing tables and recreate all tables from model
if [ "$2" == "rewrite" ]; then
    python manage.py db downgrade && \
    python manage.py db stamp head
fi

# Migrate ORM models to database. Create database and tables.
python manage.py db migrate && \
python manage.py db upgrade && \
python create_users.py

uwsgi --ini uwsgi.ini
#python manage.py runserver

