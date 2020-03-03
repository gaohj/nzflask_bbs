from django.views.decorators.http import require_POST
from .forms import LoginForm,RegisterForm
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponse
from django.shortcuts import reverse,redirect
from utils import restful_res
from utils.captcha.qfcaptcha import Captcha
from django.contrib.auth import get_user_model
from io import BytesIO
from django.core.cache import cache
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

def img_captcha(request):
    text,image = Captcha.gene_code()
    #image不能直接放到HttpResponse中返回   图片流数据
    #BytesIO管道 专门用来存放 流数据
    out = BytesIO()
    #调用image的save 将图片对象保存到 BytesIO中
    image.save(out,'png')  #保存成png格式
    out.seek(0) #将BytesIO中文件指针回到0的位置 方便读取下一张图片

    #最终还是要给浏览器 所以我们告诉浏览器这是个图片
    response = HttpResponse(content_type='image/png')

    #从管道拿出图片 保存到response对象上
    response.write(out.read())
    response['Content-lenth'] = out.tell()

    #生成图片的同时 将验证码文本写入缓存中
    cache.set(text.lower(),text.lower(),5*60)


    return response

def cache_test(request):
    cache.set('username','kangbazi',60)
    result = cache.get('username')
    print(result)
    return HttpResponse('OK')