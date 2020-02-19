from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    context = {
        'info':'<script>alert("666")</script>',
        'age':18,
    }
    return render(request,'index.html',context=context)

#http://127.0.0.1:9000/?next=/list
def login(request):
    next = request.GET.get('next')
    text = '登录完成以后要跳转的url是%s' % next
    return HttpResponse(text)

def book(request):
    return HttpResponse('图书首页')

def book_detail(request,book_id,category):
    text = '您的图书id是%s,分类是:%s' % (book_id,category)
    return HttpResponse(text)

def movie(request):
    return HttpResponse('电影首页')

def music(request):
    return HttpResponse('音乐首页')