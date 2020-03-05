from django.shortcuts import render
from .models import NewsCategory,News
from django.views.decorators.http import require_GET
from django.conf import settings
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