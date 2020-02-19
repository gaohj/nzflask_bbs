from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
# Create your views here.
from datetime import datetime
def index(request):
    #1.添加一条数据到数据库中
    # book = Book(name='程序员那些事',author='子文君',price=123.4)
    # book.save()

    # books = Book.objects.all()
    # for book in books:
    #     print(book)

    #
    # book = Book.objects.filter(name='程序员那些事',id=1)
    # print(book)

    #根据主键查找
    # book = Book.objects.get(pk=2)
    # print(book)
    # book = Book.objects.filter(name='程序员那些事').first()
    # print(book)

    # #手动排序 -表示倒序
    books = Book.objects.order_by('-pub_time')
    for book in books:
        print(book)

    #修改数据
    # book = Book.objects.get(name='程序员那些事')
    # book.pub_time = datetime.now()
    # book.save()
    #删除数据

    # book = Book.objects.get(name='程序员那些事')
    # book.delete()
    return HttpResponse('添加成功')