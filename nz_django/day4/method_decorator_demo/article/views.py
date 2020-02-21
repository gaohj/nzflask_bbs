from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods,require_GET,require_POST,require_safe
#require_GET 等同于require_http_methods(['GET'])
#require_POST 等同于require_http_methods(['POST'])
#require_safe get heade 请求 只能查看 不能修改
#等同于require_http_methods(['GET','HEAD'])
from .models import Article
#返回所有的文章  get请求
# @require_http_methods(['GET'])
# @require_GET
@require_safe
def index(request):
    articles = Article.objects.all()
    # return render(request,'index.html',context={'articles':articles})
    return HttpResponse('只能安全访问')
#get post
@require_http_methods(['GET','POST'])
def add_article(request):
    if request.method == 'GET':
        return render(request,'add.html')
    else:
        title = request.POST.get('title')
        content = request.POST.get('content')
        price = request.POST.get('price')
        Article.objects.create(title=title,content=content,price=price)
        return redirect(reverse('index'))
