from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
# Create your views here.
def index(request):
    #先将模板找到 然后编译渲染成python的字符串
    #然乎通过 HttpResponse包装成一个HttpResponse 返回给浏览器
    html = render_to_string('index.html')
    return HttpResponse(html) #参数是个字符串
def list(request):
    return render(request,'list.html')