from django.shortcuts import render
from django.http import  HttpResponse
from django.views import View
from .forms import Myform,RegisterForm
from .models import User
class IndexView(View):
    def get(self,request):
        form = Myform()
        return render(request,'index.html',context={'form':form})
    def post(self,request):
        form = Myform(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            telephone = form.cleaned_data.get('telephone')
            website = form.cleaned_data.get('website')
            return HttpResponse('ok')
        else:
            print(form.errors.get_json_data())
            return HttpResponse('fail')

class RegisterView(View):
    def get(self,request):
        form = RegisterForm()
        return render(request,'signup.html',context={'form':form})
    def post(self,request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            telephone = form.cleaned_data.get('telephone')
            password = form.cleaned_data.get('pwd1')
            User.objects.create(username=username,telephone=telephone,password=password)
            return HttpResponse('ok')
        else:
            # print(form.errors.get_json_data())
            print(form.get_errors())
            #错误信息
            #{'username': [{'message': 'Ensure this value has at least 6 characters (it has 4).', 'code': 'min_length'}], 'telephone': [{'message': '18777777777已经被注册', 'code': ''}], '__all__': [{'message': '两次密码输入不一致', 'code': ''}]}
            #{'username':['手机号已经存在','手机号不符合要求'],'telephone':[]}
            return HttpResponse('fail')