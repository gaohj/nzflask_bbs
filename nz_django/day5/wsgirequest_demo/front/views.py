from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
# Create your views here.
def index(request):
    print(request.method)
    print(request.path)
    print(request.GET.get('username'))
    return HttpResponse('index')


def login(request):
    print(request.get_host()) #127.0.0.1:8000
    print(request.get_full_path()) #/login/?username=helloword
    print(request.get_raw_uri()) #http://127.0.0.1:8000/login/?username=helloword
    print(request.is_secure()) #False
    print(request.is_ajax()) #是否是ajax 请求
    print(request.META['REMOTE_ADDR'])
    return HttpResponse('login')

def res(request):
    response = HttpResponse('<h1>千锋教育</h1>',content_type='text/html;charset=utf-8')
    response.status_code = 404
    response['X-Token'] = 'kangbazi'
    return response
import json
def json_view(request):
    persons = [
        {
            'username':'kangbazi',
            'age':18,
            'height':180
        },
        {
            'username': 'zhudaobuluke',
            'age': 20,
            'height': 200
        }
    ] #JsonResponse 只对字典 进行dump 非字典数据 必须 加上参数
    #safe=False
    # person_str = json.dumps(persons)
    # response = HttpResponse(person_str,content_type='application/json')
    # return response
    response = JsonResponse(persons,safe=False)
    return response
