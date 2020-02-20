from django.shortcuts import render
from django.http import HttpResponse
from .models import Article,Category
from front.models import FrontUser
# Create your views here.
def index(request):
    category = Category(name='伦理')
    category.save()
    article = Article(title='今天已经第15天数字连续下降',content='国难财被截止住算是保留住了最后的尊严')
    article.category = category
    article.save()
    article = Article.objects.get(pk=3)
    print(article.category.name)
    return HttpResponse('成功')
def one_to_many(request):

    article = Article(title='钢铁是怎么炼成的2',content='钢铁是怎么磨成针的2')
    author = FrontUser(username='qianghua',password='123123')
    author.save()
    article.author = author
    article.save()

    return HttpResponse('成功')