from django.shortcuts import render

def index(request):
    context = {
        'username':'qfkangbazi'
    }
    return render(request,'index.html',context=context)


def hospital(request):
    context = {
        'username':'全国真协和医院只有三家,武汉就有一家'
    }
    return render(request,'hospital.html',context=context)


def company(request):
    context = {
        'username':'现在的公司都在缩减人力成本活下去'
    }
    return render(request,'company.html',context=context)


def school(request):
    context = {
        'username': '国家不再强制网上教学了'
    }
    return render(request, 'school.html', context=context)

def supermarket(request):
    context = {
        'username': '哄抬物价，发国难财,到头来竹篮打水一场空'
    }
    return render(request, 'supermarket.html', context=context)