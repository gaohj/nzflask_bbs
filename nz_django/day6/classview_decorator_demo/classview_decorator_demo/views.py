from django.views import View
from django.http import HttpResponse
from django.shortcuts import redirect,reverse
from django.utils.decorators import method_decorator

def login_required(func):
    def wrapper(request, *args, **kwargs):
        if request.GET.get('username'):
            return func(request, *args, **kwargs)
        else:
            return redirect(reverse('login'))

    return wrapper

@login_required
def index(request):
    return HttpResponse('首页')


@method_decorator(login_required,name='dispatch')
class ProfileView(View):
    def get(self,request,*args,**kwargs):
        return HttpResponse('个人中心页面')

    # @method_decorator(login_required)
    # def dispatch(self, request, *args, **kwargs):
    #     return super(ProfileView, self).dispatch( request, *args, **kwargs)

    def http_method_not_allowed(self, request, *args, **kwargs):
        return HttpResponse('不接受get外其他请求')

#http://127.0.0.1:8000/?username=kangbazi
def login(request):
    return HttpResponse('登录页')


