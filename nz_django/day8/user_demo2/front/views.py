from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
# from .models import Person
def index(request):
    # user = User.objects.create_user('xukun','kunkun@163.com','123456')
    # user.first_name = '菜'
    # user.save()
    # user = authenticate(request,email='kaiwan@163.com',password='123456')
    # #验证通过以后 返回一个user对象
    # if user:
    #     print('%s登录成功'% user.username)
    # else:
    #     print('用户名或者密码错误')
    return render(request,'index.html')

def proxy_view(request):
    # blacklist = Person.get_blacklist()
    # for person in blacklist:
    #     print(person.username)
    return HttpResponse('代理模型')

#django自带的验证authenticate只能username和password 有了telephone 想用 手机号和密码
#需要自定义验证器

def my_authenticate(telephone,password):
    #1验证手机号
    user = User.objects.filter(extension__telephone=telephone).first()
    #2验证密码
    if user:
        is_correct = user.check_password(password)
        if is_correct:
            return user
        else:
            return None
    else:
        return None

def one_view(request):
    # user = User.objects.create_user('xcxk','xcxk@qq.com','123123')
    # user.extension.telephone = '18777777777'
    # user.extension.school = 'rap篮球'
    # user.save()
    # telephone = request.GET.get('telephone')
    # password = request.GET.get('password')
    # user = my_authenticate(telephone,password)
    # if user:
    #     print("%s验证成功" % user.username)
    # else:
    #     print('验证失败')
    return HttpResponse('一对一扩展模型')

