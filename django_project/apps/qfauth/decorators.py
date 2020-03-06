
from utils import restful_res
from django.shortcuts import redirect,reverse
def qf_login_required(func):
    def wrapper(request,*args,**kwargs):
        if request.user.is_authenticated:
            return func(request,*args,**kwargs)
        else:
            if request.is_ajax():
                return restful_res.unauth(message="请先登录")
            else:
                return redirect(reverse('news:index'))

    return wrapper