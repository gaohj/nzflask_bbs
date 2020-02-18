from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('文章首页')


def article_list(request,year):
    text = '汝输入的年份是:%s' % year
    return HttpResponse(text)

def author_tel(request,tels):
    text = '作者的手机号是:%s' % tels
    return HttpResponse(text)