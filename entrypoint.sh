#!/bin/sh

python manage.py makemigrations orders --check || python manage.py makemigrations orders
python manage.py makemigrations orders
python manage.py migrate

# Creating superuser (change login/password if you want)
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@example.com', 'admin') if not User.objects.filter(username='admin').exists() else None" | python manage.py shell

echo "Server will be available at http://localhost:8000"
exec python manage.py runserver 0.0.0.0:8000
# run in cmd
exec "$@"