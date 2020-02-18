from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('电影首页')


def movie_detail(request,movie_id):
    text = '电影id是:%s' % movie_id
    return HttpResponse(text)