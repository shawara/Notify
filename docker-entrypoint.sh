#!/bin/sh -e

# check if the database is ready
echo "Waiting for Postgres DB"
sleep 10

echo "Postgres DB is ready"
echo "Collect static files"
python3 manage.py collectstatic --no-input

# create tables
echo "Updating Database Tables"
python3 manage.py makemigrations
python3 manage.py migrate
echo "The Database has been updated"

# run the server
echo "Starting the server..."
gunicorn --bind unix:/run/notify.sock Notify.wsgi --timeout 120 ${RELOAD} --capture-output --log-level debug
