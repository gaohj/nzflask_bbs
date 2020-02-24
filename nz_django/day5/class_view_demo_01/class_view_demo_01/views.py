from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View,TemplateView
def index(request):
    return HttpResponse('这是首页')

class BookView(View):
    def get(self,request,*args,**kwargs):
        return HttpResponse("图书首页")

    def post(self,request,*args,**kwargs):
        return render(request,"post提交")

class AddBookView(View):
    def get(self,request,*args,**kwargs):
        return render(request, 'add_book.html')

    def post(self,request,*args,**kwargs):
        bookname = request.POST.get('name')
        author = request.POST.get('author')
        print("name:{},author:{}".format(bookname,author))
        return HttpResponse("成功")

class BookDetailView(View):
    def get(self,request,book_id,*args,**kwargs):
        print('图书的id是:%s' % book_id)
        return HttpResponse("成功")
    def dispatch(self, request, *args, **kwargs):
        print('不管你是什么方法都要走我这里')
        return super(BookDetailView, self).dispatch(request,*args,**kwargs)
    #跟flask 中的  dispatch_request一个道理
    def http_method_not_allowed(self, request, *args, **kwargs):
        return HttpResponse('不支持get以外其他的请求')

class AboutView(TemplateView):

    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = {"phone":"18888888888"}
        return context