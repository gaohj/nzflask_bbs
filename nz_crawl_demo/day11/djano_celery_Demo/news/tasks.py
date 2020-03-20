import time
from celery import task

@task
def task1(x,y):
    print(x+y)
    return x+y

@task
def task2(x,y):
    print(x*y)
    return x*y