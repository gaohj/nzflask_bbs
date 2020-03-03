from django.views.decorators.http import require_POST
from .forms import LoginForm,RegisterForm
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponse
from django.shortcuts import reverse,redirect
from utils import restful_res
from django.contrib.auth import get_user_model

User = get_user_model()
@require_POST
def login_view(request):
    form = LoginForm(request.POST)
    if form.is_valid():
        telephone = form.cleaned_data.get('telephone')
        password = form.cleaned_data.get('password')
        remember = form.cleaned_data.get('remember')
        user = authenticate(request,username=telephone,password=password)
        if user:
            if user.is_active:
                login(request,user)
                if remember:
                    request.session.set_expiry(None) #None默认过期时间2周
                else:
                    request.session.set_expiry(0)
                return restful_res.success()
            else:
                return restful_res.unauth(message="您的账户被冻结")
        else:
            return restful_res.params_error(message="用户名或者密码错误")
    else:
        errors = form.get_errors()
        return restful_res.params_error(message=errors)


def logout_view(request):
    logout(request)
    return redirect(reverse('cms:index'))

@require_POST
def register_view(request):
    form = RegisterForm(request.POST)
    if form.is_valid():
        telephone = form.cleaned_data.get('telephone')
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = User.objects.create_user(telephone=telephone,username=username,password=password)
        login(request,user)
        return restful_res.success()
    else:
        errors = form.get_errors()
        return restful_res.params_error(message=errors)