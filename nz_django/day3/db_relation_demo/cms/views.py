from django.shortcuts import render
from django.http import HttpResponse
from .models import Article,Category,Tag
from front.models import FrontUser,UserExtension
# Create your views here.
def index(request):
    # category = Category(name='伦理')
    # category.save()
    # article = Article(title='今天已经第15天数字连续下降',content='国难财被截止住算是保留住了最后的尊严')
    # article.category = category
    # article.save()
    # article = Article.objects.get(pk=3)
    # print(article.category.name) #查看文章的分类

    #获取分类下面所有的文章
    # category = Category.objects.first()
    #
    # articles = category.article_set.all()
    # for article in articles:
    #     print(article)
    # user = FrontUser.objects.first()
    # articles = user.article_set.all()
    # for article in articles:
    #     print(article)

    # category = Category.objects.first()
    #
    # articles = category.articles.all()
    # for article in articles:
    #     print(article)

    return HttpResponse('成功')
def one_to_many(request):

    # article = Article(title='钢铁是怎么炼成的2',content='钢铁是怎么磨成针的2')
    # author = FrontUser(username='qianghua',password='123123')
    # author.save()
    # article.author = author
    # article.save()
    # category = Category.objects.first() #获取第一个分类
    #
    # article = Article(title='除了转介绍', content='咱们之间没什么话可说')
    # article.author = FrontUser.objects.first()
    # category.articles.add(article,bulk=False)
    #如果model没有加上 related_name='articles'
    #那么我们可以使用 category.article_set.add(article,bulk=False)
    #将文章添加到分类之前 文章应该先保存
    #保存文章分类不能为空
    #文章没有分类不能保存  将文章添加到分类中 又必须保存文章
    #这就陷入一个死循环
    # bulk=False能解决这个死循环
    #django能自动的保存article 而不需要在添加到分类之前保存文章
    # user = FrontUser.objects.first()
    # articles = user.article_set.all()
    # for article in articles:
    #     print(article)

    #谁写了除了转介绍为标题的文章     模型名字的小写__字段
    # user = FrontUser.objects.filter(article__title='除了转介绍').first()
    # print(user)
    #加上related_name 这里就不能这么写了
    # user = FrontUser.objects.filter(u_articles__title='除了转介绍').first()
    # print(user)
    # 因为你加了related_query_name 相当于起了一个别名所以 related_name 那个名字直接用了
    user = FrontUser.objects.filter(u_a__title='除了转介绍').first()
    print(user)

    return HttpResponse('一对多成功')

def one_to_one(request):
    # user = FrontUser.objects.get(pk=2)
    # extension = UserExtension(school='斯坦福大学')
    # extension.user = user
    # extension.save()

    # #学校信息对应的用户是谁
    # extension = UserExtension.objects.first()
    # print(extension.user)
    #用户的学校信息
    user = FrontUser.objects.get(pk=2)
    print(user.extension)
    return HttpResponse('一对一成功')

def many_to_many(request):
    # article = Article.objects.first()
    # tag = Tag(name='冷门文章')
    # tag.save()
    # article.tag_set.add(tag)
    # article = Article.objects.first()
    # tags = article.tag_set.all() #如果模型中  articles = models.ManyToManyField('Article',related_name='tags')
    #加上了 related_name 那么 tag_set  就要替换成tags
    # for tag in  tags:
    #     print(tag)

    # article = Article.objects.get(pk=2)
    # tag = Tag.objects.first()
    # tag.articles.add(article)

    tag = Tag.objects.first()
    articles = tag.articles.all()
    for article in articles:
        print(article)
    return HttpResponse('多对对成功')

