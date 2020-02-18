from django.http import HttpResponse
from django.shortcuts import redirect,reverse
# Create your views here.
def index(request):
    #http://127.0.0.1:8000/?username=kangbazi
    # username = request.GET['username']
    username = request.GET.get('username')
    if username:
        return HttpResponse('后台首页')
    else:
        # login_url = reverse('cms:login')
        # print('='*50)
        # print(login_url)
        # print('='*50)
        # # return redirect('/signin/')
        # return redirect(login_url)
        #获取你到底是哪个实例
        current_namespace = request.resolver_match.namespace
        #获取当前的实例
        print('=' * 50)
        print(current_namespace)
        print('=' * 50)
        #实例命名空间：url名称
        #应用命名空间:url名称
        return redirect(reverse('%s:login'% current_namespace) )

def login(request):
    return HttpResponse('后台登录页面')