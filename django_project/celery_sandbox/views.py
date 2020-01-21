from django.shortcuts import render
from .tasks import add, mul


def my_request(request):

    return render(request, 'celery_sandbox_request.html')


def my_response(request):

    add.delay(1, 3)
    return render(request, 'celery_sandbox_response.html')