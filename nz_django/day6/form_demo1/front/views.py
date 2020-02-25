from django.shortcuts import render
from django.views import View
from .forms import MessageBoardForm
from django.http import HttpResponse

class IndexView(View):
   def get(self,request):
       form = MessageBoardForm()
       return render(request,'index.html',context={'form':form})

   def post(self,request):
       form = MessageBoardForm(request.POST)#实例化表单对象
       #接收post提交过来的数据
       if form.is_valid(): #判断是否符合要求
           title = form.cleaned_data.get('title')
           content = form.cleaned_data.get('content')
           email = form.cleaned_data.get('email')
           reply = form.cleaned_data.get('reply')
           print("*"*50)
           print(title)
           print(content)
           print(email)
           print(reply)
           print("*"*50)
           return HttpResponse('成功')
       else:
           print(form.errors.get_json_data())
           return HttpResponse('失败')