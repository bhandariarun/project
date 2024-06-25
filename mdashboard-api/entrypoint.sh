#!/bin/bash

# Apply Django database migrations
python manage.py migrate

# Create a superuser if it doesn't exist
DJANGO_SUPERUSER_PASSWORD=${DJANGO_SUPERUSER_PASSWORD:-zakipoint}
python manage.py shell <<EOF
from django.contrib.auth import get_user_model

User = get_user_model()
if not User.objects.filter(username='zaki').exists():
    User.objects.create_superuser('zaki', 'zaki@mail.com', '$DJANGO_SUPERUSER_PASSWORD')
else:
    print('SuperUser zaki already exists')
EOF

# Start Django development server
exec python3 manage.py runserver 0.0.0.0:8000