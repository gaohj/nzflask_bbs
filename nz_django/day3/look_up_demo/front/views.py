from django.http import HttpResponse
from .models import Article,Category
from django.utils.timezone import make_aware
# Create your views here.
def index(request):
    # article = Article(title='有了金刚钻我们再揽瓷器活',content='金刚钻都是磨出来的,所以有人成为钢板君')
    # category = Category(name='热门文章')
    # category.save()
    # category.article_set.add(article,bulk=False)
    article = Article.objects.filter(title__iexact='有了金刚钻我们再揽瓷器活')
    print(article.query) #上面如何通过sql语句进行查询
    #query只针对 QuerySet对象 不能用在普通的ORM模型 比如get 就不能使用query查看最终转成的sql语句
    #get 返回的是满足条件的ORM模型
    print(article) #返回的QuerySet对象
    return HttpResponse('成功')

def index1(request):
    article = Article.objects.get(pk=1)
    print(article.query) #因为是get 查询的
    print(article) #返回的不是QuerySet对象
    #第一个print报错
    return HttpResponse('index1成功')

def index2(request):
    article = Article.objects.filter(title__contains='金刚钻')
    print(article.query)
    print(article)
    return HttpResponse('index2成功')

def index3(request):
    # articles = Article.objects.filter(id__in=[1,2,3])
    # for article in articles:
    #     print(article)
    # print(article.query)
    # categories = Category.objects.filter(articles__in=[1,2,3])
    # for category in categories:
    #     print(category)
    # print(categories.query)
    #先把文章id为123的查出来 然后再查询他们的分类
    # articles = Article.objects.filter(title__contains='金刚钻')
    # categories = Category.objects.filter(articles__in=articles)
    # for category in categories:
    #     print(category)
    # print(categories.query)
    #获取文章中包含a字符的标题的文章分类
    categories = Category.objects.filter(articles__title__icontains='a')
    for category in categories:
        print(category)
    print(categories.query)
    return HttpResponse('index3成功')

def index4(request):
    article = Article.objects.filter(id__gt=1)
    print(article.query)
    print(article)
    return HttpResponse('index4成功')
from datetime import datetime
def index5(request):
    start_time =make_aware(datetime(year=2019,month=2,day=15,hour=8,minute=0,second=0))
    end_time = make_aware(datetime(year=2021,month=2,day=20,hour=10,minute=0,second=0))
    articles = Article.objects.filter(create_time__range=(start_time,end_time))
    for article in articles:
        print(article)
    print(articles.query)
    return HttpResponse('index5成功')

def index6(request):
    articles = Article.objects.filter(create_time__year__gt=2019)
    for article in articles:
        print(article)
    print(articles.query)
    return HttpResponse('index6成功')


def index7(request):
    articles = Article.objects.filter(title__regex=r'^a')
    for article in articles:
        print(article)
    print(articles.query)
    return HttpResponse('index7成功')