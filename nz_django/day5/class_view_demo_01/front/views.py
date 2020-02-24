from django.shortcuts import render
from .models import Article
from django.http import HttpResponse
from django.views.generic import ListView
def add_article(request):
    articles = []
    for x in range(0,108):
        article = Article(title='标题:%s'%x,content='内容:%s'%x)
        articles.append(article)
    Article.objects.bulk_create(articles)
    return HttpResponse('添加成功')


class ArticleListView(ListView):
    model = Article #指定模型
    template_name = 'article_list1.html' #模板
    context_object_name = 'articles' #渲染到模板上的对象
    paginate_by = 10 #每页展示多少条数据
    ordering = 'create_time' #列表的排序方式
    #127.0.0.1:9000/article/add/?page=1 page页码参数
    page_kwarg = 'page' #url参数 传递用户需求 想看第几页

    #获取上下文数据 简言之就是数据库中的数据
    def get_context_data(self,**kwargs):
        context = super(ArticleListView, self).get_context_data(**kwargs)
        #获取Paginator 和 Page对象
        paginator = context.get('paginator')
        page_obj = context.get('page_obj')
        # print(paginator,page_obj)
        pagination_data = self.get_pagination_data(paginator,page_obj)
        context.update(pagination_data)
        return context

    #如果不想让所有的数据都返回那么我们可以重写一个方法将不需要的数据过滤掉

    # def get_queryset(self):
    #     return Article.objects.filter(id__lte=50)

    #自定义的方法
    def get_pagination_data(self,paginator,page_obj,aroud_count=2):
        current_page = page_obj.number #当前页码 以这个为参照物
        num_pages = paginator.num_pages #总共有多少页
        left_has_more = False
        right_has_more = False

        if current_page <= aroud_count +2 :
            left_page = range(1,current_page) #如果页码小于等于五 那么直接就是12345
        else:
            left_has_more = True
            left_page = range(current_page-aroud_count,current_page)

        if current_page >= num_pages -aroud_count -1 :
            right_page = range(current_page+1,num_pages+1)  # 如果页码小于等于五 那么直接就是12345
        else:
            right_has_more = True
            #14页为例子  15 16 17   range(14+1,18)
            right_page = range(current_page+1,current_page+aroud_count+1)

        return {
            'current_page':current_page,
            'left_pages':left_page,
            'right_pages':right_page,
            'left_has_more':left_has_more,
            'right_has_more':right_has_more,
            'num_pages':num_pages
        }
