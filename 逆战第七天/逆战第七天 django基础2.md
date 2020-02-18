# 逆战第七天 django基础2  

* 视图函数  
* url  
* 模板  



## 视图函数  

> 第一个参数永远是request  这个request 存储了前端用户请求的所有的信息 （参数以及头信息）request先将数据接收 然后存储到数据库 再把执行的结果返回给浏览器 
>
> 返回的结果必须是 HttpResponse对象（HttpResponseBase的对象）

```python
from django.http import HttpResponse


def index(request): #第一个参数 永远是request
    return HttpResponse('千锋首页')


urlpatterns = [     #django会从 urlpatterns变量里边读取所有的匹配规则
    path('',index),  #规则使用 django.urls.path()函数包裹  第一个是路由第二个视图函数名  
]
```



### 给URL添加参数 

```python

book.views 
def book_detail(request,book_id,category_id):  
    text = '您获取的图书id是:%s,图书分类是:%s' % (book_id,category_id)
    return HttpResponse(text) 

#http://127.0.0.1:8000/book/author/?id=666
def author(request):
    author_id = request.GET['id']
    text = '作者的id是:%s' % author_id
    return HttpResponse(text)
    
urls.py 

from book import views
urlpatterns = [
    ...
    path('book/detail/<book_id>/<category_id>/', views.book_detail),
    path('book/author/', views.author),

]
```



### urls包含另外一个urls  

```python
book 

views.py 

def index(request):
    return HttpResponse('图书首页')

def book_detail(request,book_id):
    text = '图书id是:%s' % book_id
    return HttpResponse(text)
    
urls.py 

from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('detail/<book_id>/', views.book_detail),
]

movie  

views.py

def index(request):
    return HttpResponse('电影首页')


def movie_detail(request,movie_id):
    text = '电影id是:%s' % movie_id
    return HttpResponse(text)
    
urls.py 

from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('detail/<movie_id>/', views.movie_detail),
]


urls.py
from django.urls import path,include
#http://www.douban.com/book/list
#http://www.douban.com/movie/list
urlpatterns = [
    path('book/',include('book.urls')),
    path('movie/',include('movie.urls')),
]


#如果 你没有在应用中 写 urls  也可以使用include 包含的方式  

from django.urls import path,include
from movie import views as movie
from music import views as music
#http://www.douban.com/book/list
#http://www.douban.com/movie/list
urlpatterns = [
    path('book/',include('book.urls')),
    path('movie/',include([
        path('',movie.index),
        path('detail/<movie_id>/',movie.movie_detail)
    ])),
    path('music/',include([
        path('',music.index),
        path('detail/<music_id>/',music.music_detail)
    ])),

]
```



### path函数  

```
 path('detail/<int:book_id>/', views.book_detail), 
 
 
 (route, view, kwargs=None, name=None)
 
 route参数:
 <类型:参数名>
 
 str:非空字符串  不包含斜杠  /
 int:任意的0或者正整数
 slug:半角- _ 英文字符 或者 数字组成的字符串  
 uuid： f71f1639-b0ff-49cd-824c-4612c678fdb5   uuid.uuid4() 
 path:非空英文字符串  包含/  
 
 view参数
 1.视图函数名字 
 2.类视图.as_view()
 3.django.urls.include()函数的返回值  
 
 
 name参数 
 
 1.给url起名字用的  项目比较大url比较多的时候 很重要  
 
 
 kwargs  
 
 1.给视图函数传递额外的参数用的   
 	
     path('detail/<int:book_id>/', views.book_detail,{'name':'kangbazi'}),
	 def book_detail(request,book_id,name):
    	text = '图书id是:%s,名称是:%s' % (book_id,name)
    	return HttpResponse(text)
 
 
```



### re_path 

> path函数如果不满足我们的复杂要求 这个时候我们可以写正则表达式   通过re_path即可  

```python
views.py 

from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('文章首页')


def article_list(request,year):
    text = '汝输入的年份是:%s' % year
    return HttpResponse(text)

def author_tel(request,tels):
    text = '作者的手机号是:%s' % tels
    return HttpResponse(text)

articles.urls 

from django.urls import re_path
from . import views


urlpatterns = [
    #r'' 表示原生字符串
    re_path(r'^$',views.index),
    re_path(r'^list/(?P<year>\d{4})/$',views.article_list),
    re_path(r'^author/(?P<tels>1[3-9]\d{9})/$',views.author_tel),
]
```

