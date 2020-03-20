from django.shortcuts import render
from .tasks import task1,task2
from django.http import JsonResponse

def do_task1(request):
    task1.delay(10,20)
    return JsonResponse({'msg':'task1ok'})

def do_task2(request):
    task2.delay(30,40)
    return JsonResponse({'msg': 'task2ok'})


