from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
def index(request):
    # user = User.objects.create_user('xiaowen','wenzai@163.com','123123') #创建普通用户
    # user.first_name = 'chengcheng'  #其它属性赋值
    # user.last_name = 'wenwen'
    # user.save()
    # user = User.objects.create_superuser('root','root@linux.com','111111') #创建超级用户
    #修改密码
    # user = User.objects.get(pk=1)
    # user.set_password('654321')
    # user.save()
    user = authenticate(username='daoke',password='6543213')
    if user:
        print("%s登录成功" % user.username)
    else:
        print("用户名或者密码错误")
    return render(request,'index.html')
