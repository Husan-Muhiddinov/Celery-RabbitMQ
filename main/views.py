from django.shortcuts import render
from django.http import HttpResponse
from .tasks import slow_func
# Create your views here.


# def slow_func(num):
#     for i in range(num):     # Bu funksiyani working qilib  celery va RabbitMQ da ishlatdik 
#         print(i)          # Abdurasulov Codes

def index(request):
    slow_func.delay(1234567)
    return HttpResponse('Site is Working!')

