worker: python manage.py celery worker
web: python manage.py collectstatic --noinput; python manage.py run_gunicorn -b 0.0.0.0:$PORT