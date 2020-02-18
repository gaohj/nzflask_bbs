from django.http import HttpResponse
from django.shortcuts import reverse

# Create your views here.
def article(request):
    return HttpResponse('文章首页')

def article_list(request,categories):
    print('categories:%s'%categories)
    print(reverse('list',kwargs={'categories':categories}))
    text = '您填写的分类是:%s' % categories
    return HttpResponse(text)

def article_detail(request,article_id):
    print(reverse('detail',kwargs={'article_id':article_id}))
    text = '您要查看的文章是:%s' % article_id
    return HttpResponse(text)