from django.shortcuts import render
from datetime import datetime
def greet(word):
    return 'hello world %s' % word


def index(request):
    context = {
        'mytime':datetime(year=2020,month=2,day=18,hour=18,minute=16,second=30)
    }
    return render(request,'index.html',context=context)

def add_view(request):
    context = {
        'value1': ['1','2','3'],
        'value2': ['4','5',6],
    }
    return render(request, 'add.html', context=context)

def default_view(request):
    context = {
        'value':None
    }
    return render(request, 'default.html', context=context)