from django.shortcuts import render,redirect,reverse
from .models import User
from django.views import View
from .forms import SignupForm,SigninForm
from django.contrib import messages
def index(request):
    # users = []
    # for x in range(0,51):
    #     user = User(username='用户名:%s'%x,password='password:%s'% x,telephone='138123456:%s'%x)
    #     users.append(user)
    # User.objects.bulk_create(users)
    users = User.objects.all()
    context = {
        'users':users
    }
    return render(request,'index.html',context=context)

class SigninView(View):
    def get(self,request):
        return render(request,'signin.html')
    def post(self,request):
        form = SigninForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = User.objects.filter(username=username,password=password).first()
            if user:
                request.session['user_id'] = user.id
                return redirect(reverse('index'))
            else:
                 # print('用户名或者密码错误')
                 messages.info(request,'用户名或者密码错误')
                 return redirect(reverse('signin'))
        else:
            # print(form.get_errors())
            errors = form.get_errors() #结果是列表
            for error in errors:
                messages.info(request,error)
            return redirect(reverse('signin'))


class SignupView(View):
    def get(self,request):
        return render(request,'signup.html')
    def post(self,request):
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('index'))
        else:
            print(form.errors.get_json_data())
            return redirect(reverse('signup'))

def logout(request):
    #request.session.clear() #清除当前用户的session
    request.session.flush() #清除当前用户的session并且删除浏览器存储的session_id 注销一般用这个
    return redirect(reverse('index'))


def blog(request):
    return render(request,'blog.html')
def video(request):
    return render(request,'video.html')