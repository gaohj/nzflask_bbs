from django.shortcuts import render,redirect,reverse
from django.db import connection
def get_corsor():
    return connection.cursor()

# Create your views here.
#主要是用来展示所有的图书列表
def index(request):
    cursor = get_corsor()
    cursor.execute("select id,name,author from book")
    books = cursor.fetchall()
    print(books)
    #(),()
    context = {
        'books':books
    }
    return render(request,'index.html',context=context)

def add_book(request):
    if request.method == 'GET': #django 判断请求方式
        error=''
        return render(request, 'add_book.html',context={'error':error})
    else:
        name = request.POST.get('name')
        author = request.POST.get('author')
        cursor = get_corsor()
        cursor.execute("insert into book(id,name,author) values (null,'%s','%s')" %(name,author))

        return redirect(reverse('index'))

def book_detail(request,book_id):
    cursor = get_corsor()
    cursor.execute("select id,name,author from book where id=%s" % book_id)
    book = cursor.fetchone()
    return render(request,'book_detail.html',context={"book":book})

def delete_book(request):
    if request.method == 'POST':
        book_id = request.POST.get('book_id')
        cursor = get_corsor()
        cursor.execute("delete from book where id=%s" % book_id)
        return redirect(reverse('index'))
    else:
        raise RuntimeError('删除图书的方法错误')
