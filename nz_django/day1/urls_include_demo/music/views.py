from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('音乐首页')


def music_detail(request,music_id):
    text = '音乐id是:%s' % music_id
    return HttpResponse(text)