from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .forms import ArticleForm
from .models import Article
class IndexView(View):
    def get(self,request):
        return render(request,'index.html')
    # def post(self,request):
    #     myfile = request.FILES.get('thumbnail')
    #     with open('somefile.txt','wb') as fp:
    #         for chunk in myfile.chunks():
    #             fp.write(chunk)
    #     return HttpResponse('ok')
    # def post(self,request):
    #     title = request.POST.get('title')
    #     content = request.POST.get('content')
    #     myfile = request.FILES.get('thumbnail')
    #     Article.objects.create(title=title,content=content,thumbnail=myfile)
    #     return HttpResponse('ok')
    #
    def post(self,request):
        form = ArticleForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('ok')
        else:
            print(form.errors.get_json_data)
            return HttpResponse('fail')