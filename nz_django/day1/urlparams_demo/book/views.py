from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('图书首页')

def book_detail(request,book_id,category_id):
    text = '您获取的图书id是:%s,图书分类是:%s' % (book_id,category_id)
    return HttpResponse(text)

#http://127.0.0.1:8000/book/author/?id=666
def author(request):
    author_id = request.GET['id']
    text = '作者的id是:%s' % author_id
    return HttpResponse(text)