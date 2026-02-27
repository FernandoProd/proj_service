#!/bin/sh

python manage.py migrate

# Creating superuser (change login/password if you want)
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@example.com', 'admin') if not User.objects.filter(username='admin').exists() else None" | python manage.py shell

# run in cmd
exec "$@"