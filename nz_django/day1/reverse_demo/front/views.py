from django.http import HttpResponse
from django.shortcuts import reverse,redirect
# Create your views here.
def index(request):
    #http://127.0.0.1:8000/?username=kangbazi
    # username = request.GET['username']
    username = request.GET.get('username')
    if username:
        return HttpResponse('首页')
    else:
        # login_url = reverse('login')
        # login_url = reverse('应用命名空间:login')
        # login_url = reverse('实例命名空间:login')
        # return redirect(login_url)
        # detail_url = reverse('detail',kwargs={'artice_id':50,'page':10})
        # return redirect(detail_url)
        login_url = reverse('login') + '?next=/'
        return redirect(login_url)



def login(request):
    return HttpResponse('登录页面')


def article_detail(request,artice_id,page):
    text = '您此刻正在阅读第%s篇文章,第%s页' % (artice_id,page)
    return HttpResponse(text)