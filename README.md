# django-celery-redis-beat-flower

Need 3 servers to install
1) Redis server
2) Celery server
3) Flower

start servers 
1) Redis
redis-server

2) celery
from django_project path , celery -A django_project worker -l info

3) Celery beat
Need install django-celery-beat and add it on apps in settings.py

run celery beat in seperate terminal
celery -A djano_project beat -l info

4) Flower
run flower, celery -A django_project flower

