web: gunicorn networq.wsgi
release: python manage.py makemigrations cards && python manage.py makemigrations users && python manage.py migrate