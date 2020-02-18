from django.http import HttpResponse
from django.shortcuts import redirect,reverse
# Create your views here.
def index(request):
    #http://127.0.0.1:8000/?username=kangbazi
    # username = request.GET['username']
    username = request.GET.get('username')
    if username:
        return HttpResponse('前台首页')
    else:
        #应用命名空间：url名称
        login_url = reverse('front:login')
        print('='*50)
        print(login_url)
        print('='*50)
        # return redirect('/signin/')
        return redirect(login_url)

def login(request):
    return HttpResponse('前台登录页面')