from django.shortcuts import render
from .models import NewsCategory,News
from django.views.decorators.http import require_GET
from django.conf import settings
from .serializers import NewsSerializers
from utils import restful_res
from django.conf import settings
from django.http import Http404
@require_GET
def index(request):
    count = settings.ONE_PAGE_NEWS_COUNT
    newses = News.objects.select_related('author','category').all()[0:count]
    categories = NewsCategory.objects.all()
    context = {
        'newses':newses,
        'categories':categories
    }
    return render(request,'news/index.html',context=context)

def news_list(request):
    page = int(request.GET.get('p',1))
    #1 0 3
    #2 3 6
    #3 6 9
    # start = (第几页-1)*每页显示的条数
    start = (page-1)* settings.ONE_PAGE_NEWS_COUNT
    end = start+ settings.ONE_PAGE_NEWS_COUNT
    newses = News.objects.select_related('category','author').all()[start:end]
    serializer = NewsSerializers(newses,many=True)
    data = serializer.data
    return restful_res.result(data=data)

def news_detail(request,news_id):
    try:
        news = News.objects.select_related('category','author').get(pk=news_id)
        context = {
            'news':news
        }
        return render(request,'news/news_detail.html',context=context)
    except News.DoesNotExist:
        raise Http404
