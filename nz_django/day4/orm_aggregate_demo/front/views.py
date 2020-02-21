from django.http import HttpResponse
from .models import Book,Author,BookOrder,Publisher
from django.db.models import Avg,Count,Max,Min,Sum,F,Q
# Create your views here.
from django.db import connection
#获取所有图书的定价的平均价格
def index(request):
    result = Book.objects.aggregate(avgaaa=Avg('price'))
    print(result)
    # print(result.query) 因为返回的不是QuerySet 所以不能用query
    print(connection.queries[-1])
    return HttpResponse('index')

#获取每一本图书销售的平均价格
def index1(request):
    # result = Book.objects.aggregate(avg=Avg('bookorder__price'))
    # print(result) aggregate 所有图书的
    # print(result.query) 因为返回的不是QuerySet 所以不能用query
    books = Book.objects.annotate(avg=Avg('bookorder__price'))
    for book in books:
        print('%s/%s' %(book.name,book.avg))

    print(connection.queries[-1])
    return HttpResponse('index1')

def index2(request):
    #总共有多少本书
    # result = Book.objects.aggregate(book_nums=Count('id'))
    # print(result) #aggregate 所有图书的

    #作者表中总共有多少个不同的邮箱
    result = Author.objects.aggregate(email_nums=Count('email',distinct=True))
    print(result)

    #每一本书的销量
    # books = Book.objects.annotate(book_nums=Count('bookorder__id'))
    # #Count('bookorder__id') 可以写成Count('bookorder') 默认找主键
    # for book in books:
    #     print('%s/%s' %(book.name,book.book_nums))

    print(connection.queries[-1])
    return HttpResponse('index2')

def index3(request):
    #每一本图书售卖的时候的最大价格和最小价格
    books = Book.objects.annotate(max=Max('bookorder__price'),min=Min('bookorder__price'))
    #Count('bookorder__id') 可以写成Count('bookorder') 默认找主键
    for book in books:
        print('%s/%s/%s' %(book.name,book.max,book.min))

    print(connection.queries[-1])
    return HttpResponse('index3')

def index4(request):
    #所有图书的销售总额
    # result = BookOrder.objects.aggregate(total=Sum('price'))
    # print(result)



    #每一本图书的销售总额
    # books = Book.objects.annotate(total=Sum("bookorder__price"))
    # for book in books:
    #     print('%s/%s' %(book.name,book.total))

    #2018年度销售总额
    # result = BookOrder.objects.filter(create_time__year=2018).aggregate(total=Sum('price'))
    # print(result)

    #每一本图书在2019年度的销售的总额
    books = Book.objects.filter(bookorder__create_time__year=2019).annotate(total=Sum("bookorder__price"))
    for book in books:
        print('%s/%s' %(book.name,book.total))


    print(connection.queries[-1])
    return HttpResponse('index4')

def index5(request):
    #给每本图书售价增加8元
    # Book.objects.update(pages=F('pages')-10)
    authors = Author.objects.filter(name=F('email'))
    for author in authors:
        print('%s:%s' % (author.name,author.email))
    print(connection.queries[-1])
    return HttpResponse('index5')

def index6(request):
    #价格大于100 并且评分大于等于4.8的图书 &
    # books = Book.objects.filter(price__gte=100,rating__gte=4.8)
    # print(books)
    #如果想实现或者 那么就不好实现了
    #并且
    #books = Book.objects.filter(Q(price__gte=100)&Q(rating__gte=4.8))
    #或者
    #books = Book.objects.filter(Q(price__lte=100)|Q(rating__lte=4))
    books = Book.objects.filter(Q(price__lte=100)&~Q(name__icontains='记'))
    print(books)
    print(connection.queries[-1])
    return HttpResponse('index6')