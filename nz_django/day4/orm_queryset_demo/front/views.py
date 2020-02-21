from django.http import HttpResponse
from .models import Book,Author,BookOrder,Publisher
from django.db.models.manager import Manager
from django.db.models import F,Count,Prefetch
from django.db import connection
def index(request):
    print(type(Book.objects))
    #<class 'django.db.models.manager.Manager'>
    #objects 是django.db.models.manager.Manager的对象
    #我们追加过去发现是空壳类
    #annotate\aggragate\update\order_by 这些方法哪里来的
    #这些方法全部都是通过 python的动态添加的方式从
    #QuerySet类中拷贝过来的
    return HttpResponse('index')

def index2(request):
    #链式调用
    # books = Book.objects.filter(id__gte=2).exclude(id=3)
    # for book in books:
    #     print(book)
    # print(books.query) #filter\exclude 可以用 get 不能用
    books = Book.objects.annotate(author_name=F('author__name'))
    for book in books:
        print('%s:%s' %(book.name,book.author_name))
    print(connection.queries[-1])
    return HttpResponse('index2')

def index3(request):
    #排序
    # orders = BookOrder.objects.order_by("create_time")
    # orders = BookOrder.objects.order_by("-create_time")
    # orders = BookOrder.objects.order_by("-create_time","-price")
    #排序根据两个字段 如果第一个字段结果是一样的 那么就根据第二个字段

    #下面的结果是 第一个不生效被忽略 按照第二个条件进行排序
    # orders = BookOrder.objects.order_by('-create_time').order_by('-price')
    # for order in  orders:
    #     print("%s:%s:%s" % (order.id,order.create_time,order.price))
    #图书销量 从大到小进行排序
    books = Book.objects.annotate(order_nums=Count('bookorder')).order_by('order_nums')
    for book in  books:
        print("%s:%s" % (book.name,book.order_nums))
    print(connection.queries[-1])
    return HttpResponse('index3')


def index4(request):
    #select * from book;
    #select id,name,author from book;
    # books = Book.objects.values('name',authors=F("author__name"))
    books = Book.objects.values_list('name',flat=True) #只有参数为一个时才使用flat
    #不用flat 结果是 :('水浒传',)
    #用flat 结果是:三国演义
    print(type(books)) #QuerySet
    for book in books:
        print(book) #{'name': '金什么梅', 'authors': '曹雪芹'}
    print(connection.queries[-1])
    return HttpResponse('index4')

def index5(request):
    books = Book.objects.all()
    books = Book.objects.select_related("author","publisher")
    for book in books:
        print(book.author.name)
        print(book.publisher.name)
    #这样的结果是 先查出五条记录然后每条记录分别去作者表出版社表中进行查询
    #每一条记录需要三次查询
    print(connection.queries[-1])
    return HttpResponse('index5')

def index6(request):
    # books = Book.objects.prefetch_related("bookorder_set")
    # for book in books:
    #     print("*"*50)
    #     print(book.name)
    #     orders = book.bookorder_set.all()
    #     for order in orders:
    #         print(order.id)
    # books = Book.objects.prefetch_related('author')
    # for book in books:
    #     print(book.author.name)
    prefetch = Prefetch("bookorder_set",queryset=BookOrder.objects.filter(price__gte=90))
    books = Book.objects.prefetch_related(prefetch)
    #为了减少关联查询的次数  prefetch_related
    #但是 如果加上 filter条件 那么优势就没了
    #既想减少查询的次数  又想 加上条件
    #我们讲filter放到 django.db.models.Prefetch中 提前生成Queryset对象
    #这样的话 就不会破坏prefetch_related的优势
    for book in books:
            print("*"*50)
            print(book.name)
            orders = book.bookorder_set.all()
            for order in orders:
                print(order.id)
    print(connection.queries[-1])
    return HttpResponse('index6')

def index7(request):
    # books = Book.objects.defer('name')
    # for book in books:
    #     print(book.name)
    books = Book.objects.only('name')
    for book in books:
        print("%s/%s" % (book.id,book.price))
    print(connection.queries[-1])
    return HttpResponse('index7')

def index8(request):
    # book = Book.objects.get(pk=1)
    # print(book)
    # publisher =Publisher.objects.create(name="知音出版社")
    # result =Publisher.objects.get_or_create(name="知音888出版社")
    # print(type(result))
    # print(result)
    publisher = Publisher.objects.bulk_create([
        Publisher(name='你一口'),
        Publisher(name='他一口'),
        Publisher(name='上个厕所也手拉手'),

    ])
    print(connection.queries[-1])
    return HttpResponse('index8')

def index9(request):
    # result = Book.objects.filter(name='三国演义').exists()
    # print(result)
    result = Book.objects.count()
    print(result)
    print(connection.queries[-1])
    return HttpResponse('index9')

def index10(request):
    books = Book.objects.filter(bookorder__price__gte=80).order_by('bookorder__price').distinct()
    for book in books:
        print(book)
    print(connection.queries[-1])
    return HttpResponse('index10')


def index11(request):
    # Book.objects.update(pages=F('pages')-10)
    # books = Book.objects.all()
    # for book in books:
    #     book.price = book.price-10
    #     book.save()
    Author.objects.filter(id__gte=3).delete()
    return HttpResponse('index11')


def index12(request):
    pubs = Publisher.objects.all()[4:8] #不包含4 包含 8
    #从4截取到8
    for pub in pubs:
        print(pub)
    print(connection.queries[-1])
    return HttpResponse('index12')
@app.route('/',methos=['GET','POST'])
def index13(request):
    pubs = Publisher.objects.all() #不包含4 包含 8
    print(connection.queries) #像all()这种情况 没有牵扯到打印
    #那么不会转成sql语句去执行
    return HttpResponse('index13')