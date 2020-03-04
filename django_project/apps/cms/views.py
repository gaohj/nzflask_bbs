from django.shortcuts import render
from django.views.decorators.http import require_GET,require_POST
from django.views.generic import View
from apps.news.models import NewsCategory,News,Comment
from utils import restful_res
from django.views.decorators.http import require_POST,require_GET
from .forms import WriteNewsForm
@require_GET
def index(request):
    return render(request,'cms/index.html')

#分类页面
@require_GET
def news_category(request):
    categories = NewsCategory.objects.all()
    context = {
        'categories':categories
    }
    return render(request,'cms/news_category.html',context=context)
#添加文章分类
@require_POST
def add_news_category(request):
    name = request.POST.get('name')
    exists = NewsCategory.objects.filter(name=name).exists()
    if not exists:
        NewsCategory.objects.create(name=name)
        return restful_res.success()
    else:
        return restful_res.params_error(message='该分类已经存在')

#发布资讯

class WriteNewsView(View):
    def get(self,request):
        categories = NewsCategory.objects.all()
        context = {
            'categories':categories
        }
        return render(request,'cms/write_news.html',context=context)
    def post(self,request):
        form = WriteNewsForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            desc = form.cleaned_data.get('desc')
            content = form.cleaned_data.get('content')
            thumbnail = form.cleaned_data.get('thumbnail')
            category_id = form.cleaned_data.get('category')
            category = NewsCategory.objects.get(pk=category_id)
            print(title,content,thumbnail)
            News.objects.create(title=title,desc=desc,content=content,thumbnail=thumbnail,author=request.user,category=category)
            return restful_res.success()
        else:
            return restful_res.params_error(message=form.get_errors())
import qiniu
from django.conf import settings
def qiniu_token(request):
    access_key = settings.QINIU_ACCESS_KEY
    secret_key = settings.QINIU_SECRET_KEY
    bucket = settings.QINIU_BUCKET_NAME

    q = qiniu.Auth(access_key,secret_key)
    token = q.upload_token(bucket)

    return restful_res.result(data={"token":token})