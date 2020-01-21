# django-celery-redis-beat

Need 2 servers to install
1) Redis server
2) Celery server


start servers 
1) redis-server

from django_project path , celery -A django_project worker -l info

Need install django-celery-beat and add it on apps in settings.py


run celery beat in seperate terminal
celery -A djano_project beat -l info

