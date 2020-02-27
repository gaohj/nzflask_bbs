from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
# from django.contrib.auth.models import User
from .models import User
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

def inherit_view(request):
    # telephone = '18666666666'
    # password = '123456'
    # username='kangbazi'
    # email = 'kangbazi@aliyun.com'
    # user = User.objects.create_user(telephone=telephone,password=password,username=username,email=email)

    # print(user.username)

    #验证用户名和密码
    # user = authenticate(username='18666666666',password='123456')
    # if user:
    #     print("%s验证成功"% user.username)
    # else:
    #     print('验证失败')
    # return HttpResponse('继承自AbstractUser模型')

    # User.objects.create_user(telephone='18888888888',username='kangbazi',password='123456',email='kangbazi@1000phone.com')
    # User.objects.create_superuser(telephone='18999999999',username='kangbazi666',password='123123',email='kangbazi888@1000phone.com')
    user = authenticate(username='18999999999',password='123123')
    if user:
        print("%s验证成功"% user.username)
    else:
        print('验证失败')
    return HttpResponse('继承自AbstractBaseUser模型')

#命名的时候避开login logout因为django自己也封装了一个login logour方法
from .forms import LoginForm
from django.contrib.auth import login,logout
def my_login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            telephone = form.cleaned_data.get('telephone')
            password = form.cleaned_data.get('password')
            remember = form.cleaned_data.get('remember')
            user = authenticate(request,username=telephone,password=password)#返回一个user对象
            if user and user.is_active:
                #登录
                login(request,user)
                if remember:
                    #None 表示使用全局的过期时间 两周
                    request.session.set_expiry(None)
                else:
                    request.session.set_expiry(0)
                next_url = request.GET.get('next')
                if next_url:
                    return redirect(next_url)
                else:
                    return redirect(reverse('index'))
            else:
                return HttpResponse("用户名或者密码错误")
        else:
            print(form.errors)
            return redirect(reverse('signin'))


def my_logout(request):
    logout(request)
    return redirect(reverse('signin'))

from django.contrib.auth.decorators import login_required

@login_required(login_url='/signin/') #参数为登录的url地址
def profile(request):
    return HttpResponse("个人中心页面")

from .models import Article
from django.contrib.auth.models import ContentType
from django.contrib.auth.models import Permission

def add_permission(request):
    #给哪个模型添加权限 先获取该模型的content_type_id
    #从content_type表中获取
    content_type = ContentType.objects.get_for_model(Article)
    permission = Permission.objects.create(codename='black_list',name='拉黑文章',content_type=content_type)
    return HttpResponse("权限创建成功")

def operate_permission(request):
    #创建用户对象
    user = User.objects.first()
    #如果先给用户操作文章的权限 应该先把文章相关的权限找出来  然后绑定在用户上面
    #查找文章对应的content_type_id
    content_type = ContentType.objects.get_for_model(Article)
    permissions = Permission.objects.filter(content_type=content_type)
    # user.user_permissions.add(permissions[0])
    # user.save()
    # for permission in permissions:
    #     print(permission)
    user.user_permissions.set(permissions)
    user.save()
    # user.user_permissions.clear()#清空权限
    #user.user_permissions.remove(*permissions)#清空权限
    # user.user_permissions.remove(permissions[0])#清空权限
    if user.has_perm('front.view_article'):
        print('拥有view_article这个权限')
    else:
        print('没有view_article这个权限')
    print(user.get_all_permissions()) #字典
    return HttpResponse("操作权限成功")


from django.contrib.auth.decorators import permission_required

@permission_required(['front.add_article','front.view_article'],login_url='/signin/',raise_exception=True)
def add_article(request):
    # #判断用户是否登录了
    # if request.user.is_authenticated:
    #     print('您已经登录')
    # #判断是否有这个权限
    #     if request.user.has_perm('front.add_article'):
    #         return HttpResponse('这是添加文章的页面')
    #     #如果没有权限 让你重新换个有权限的账户登录
    #     else:
    #         return HttpResponse('您没有相关权限奥利给',status=403)
    # else:
    #     return redirect(reverse('signin'))
    return HttpResponse('这是添加文章的页面')



#添加分组 给组添加权限  创建用户以后 把他加入到指定的组里
#  不再一个个添加权限
from django.contrib.auth.models import Group
def operate_group(request):
    # group = Group.objects.create(name='管理员')
    content_type = ContentType.objects.get_for_model(Article)
    permissions = Permission.objects.filter(content_type=content_type)
    # group.permissions.set(permissions)
    # group.save()
    # group = Group.objects.first() #获取指定的组
    # user = User.objects.first()
    # user.groups.add(group)
    # user.save()

    user = User.objects.first()
    permissions = user.get_group_permissions()
    print(permissions)

    if user.has_perms(['front.add_article', 'front.view_article']):
        print('y')
    else:
        print('n')
    return HttpResponse('这是操作组')

