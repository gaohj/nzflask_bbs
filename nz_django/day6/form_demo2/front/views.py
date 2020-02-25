from django.shortcuts import render
from django.http import  HttpResponse
from django.views import View
from .forms import Myform
class IndexView(View):
    def get(self,request):
        return render(request,'index.html')
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