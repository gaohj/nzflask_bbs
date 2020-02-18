from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('图书首页')


def book_detail(request,book_id,name):
    text = '图书id是:%s,名称是:%s' % (book_id,name)
    return HttpResponse(text)