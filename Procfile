release: python manage.py migrate -a note
web: gunicorn note.wsgi:application --log-file -