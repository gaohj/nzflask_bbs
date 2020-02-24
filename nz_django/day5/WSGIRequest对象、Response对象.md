# WSGIRequest对象

Django在接收到http请求之后，会根据http请求携带的参数以及报文信息创建一个`WSGIRequest`对象，并且作为视图函数第一个参数传给视图函数。也就是我们经常看到的`request`参数。在这个对象上我们可以找到客户端上传上来的所有信息。这个对象的完整路径是`django.core.handlers.wsgi.WSGIRequest`。

## WSGIRequest对象常用属性和方法：

### WSGIRequest对象常用属性：

`WSGIRequest`对象上大部分的属性都是只读的。因为这些属性是从客户端上传上来的，没必要做任何的修改。以下将对一些常用的属性进行讲解： 

1. `path`：请求服务器的完整“路径”，但不包含域名和参数。比如`http://www.baidu.com/xxx/yyy/`，那么`path`就是`/xxx/yyy/`。 

2. `method`：代表当前请求的`http`方法。比如是`GET`还是`POST`。request.method == 'POST':

3. `GET`：一个`django.http.request.QueryDict`对象。操作起来类似于字典。这个属性中包含了所有以`?xxx=xxx`的方式上传上来的参数。 request.GET.get()

4. `POST`：也是一个`django.http.request.QueryDict`对象。这个属性中包含了所有以`POST`方式上传上来的参数。 request.POST.get()

5. `FILES`：也是一个`django.http.request.QueryDict`对象。这个属性中包含了所有上传的文件。 

6. `COOKIES`：一个标准的Python字典，包含所有的`cookie`，键值对都是字符串类型。 

7. `session`：一个类似于字典的对象。用来操作服务器的`session`。 

8. `META`：存储的客户端发送上来的所有`header`信息。

9. `CONTENT_LENGTH`：请求的正文的长度（是一个字符串）。

10. `CONTENT_TYPE`：请求的正文的MIME类型。

11. `HTTP_ACCEPT`：响应可接收的Content-Type。

12. `HTTP_ACCEPT_ENCODING`：响应可接收的编码。

13. `HTTP_ACCEPT_LANGUAGE`： 响应可接收的语言。

14. `HTTP_HOST`：客户端发送的HOST值。

15. `HTTP_REFERER`：在访问这个页面上一个页面的url。

16. `QUERY_STRING`：单个字符串形式的查询字符串（未解析过的形式）。

17. `REMOTE_ADDR`：客户端的IP地址。如果服务器使用了`nginx`
    
    做反向代理或者负载均衡，那么这个值返回的是`127.0.0.1`，这时候可以使用`HTTP_X_FORWARDED_FOR`来获取，所以获取ip地址的代码片段如下：

    ```python
    if request.META.has_key('HTTP_X_FORWARDED_FOR'):  
          ip =  request.META['HTTP_X_FORWARDED_FOR']  
      else:  
          ip = request.META['REMOTE_ADDR']
    ```
18. `REMOTE_HOST`：客户端的主机名。

19. `REQUEST_METHOD`：请求方法。一个字符串类似于`GET`或者`POST`。

20. `SERVER_NAME`：服务器域名。

21. `SERVER_PORT`：服务器端口号，是一个字符串类型。

### WSGIRequest对象常用方法：

1. `is_secure()`：是否是采用`https`协议。
2. `is_ajax()`：是否采用`ajax`发送的请求。原理就是判断请求头中是否存在`X-Requested-With:XMLHttpRequest`。
3. `get_host()`：服务器的域名。如果在访问的时候还有端口号，那么会加上端口号。比如`www.baidu.com:9000`。
4. `get_full_path()`：返回完整的path。如果有查询字符串，还会加上查询字符串。比如`/music/bands/?print=True`。
5. `get_raw_uri()`：获取请求的完整`url`。

## QueryDict对象：

我们平时用的`request.GET`和`request.POST`都是`QueryDict`对象，这个对象继承自`dict`，因此用法跟`dict`相差无几。其中用得比较多的是`get`方法和`getlist`方法。 

1. `get`方法：用来获取指定`key`的值，如果没有这个`key`，那么会返回`None`。 
2. `getlist`方法：如果浏览器上传上来的`key`对应的值有多个，那么就需要通过这个方法获取。

# HttpResponse对象

Django服务器接收到客户端发送过来的请求后，会将提交上来的这些数据封装成一个`HttpRequest`对象传给视图函数。那么视图函数在处理完相关的逻辑后，也需要返回一个响应给浏览器。而这个响应，我们必须返回`HttpResponseBase`或者他的子类的对象。而`HttpResponse`则是`HttpResponseBase`用得最多的子类。那么接下来就来介绍一下`HttpResponse`及其子类。

## 常用属性：

1. content：返回的内容。

2. status_code：返回的HTTP响应状态码。

3. content_type：返回的数据的MIME类型，默认为`text/html`。浏览器会根据这个属性，来显示数据。如果是

   `text/html`，那么就会解析这个字符串，如果`text/plain`，那么就会显示一个纯文本。常用的
   
   `Content-Type`如下：

   - text/html（默认的，html文件）
- text/plain（纯文本）
   - text/css（css文件）
   - text/javascript（js文件）
   - multipart/form-data（文件提交）
   - 文件上传  
- application/json（json传输）
   - application/xml（xml文件）

4. 设置请求头：`response['X-Access-Token'] = 'xxxx'`。

## 常用方法：

1. set_cookie：用来设置`cookie`信息。后面讲到授权的时候会着重讲到。
2. delete_cookie：用来删除`cookie`信息。
3. write：`HttpResponse`是一个类似于文件的对象，可以用来写入数据到数据体（content）中。

## JsonResponse类：

用来对象`dump`成`json`字符串，然后返回将`json`字符串封装成`Response`对象返回给浏览器。并且他的`Content-Type`是`application/json`。示例代码如下：

```python
from django.http import JsonResponse
def index(request):
    return JsonResponse({"username":"千锋","age":18})
```

默认情况下`JsonResponse`只能对字典进行`dump`，如果想要对非字典的数据进行`dump`，那么需要给`JsonResponse`传递一个`safe=False`参数。示例代码如下：

```python
from django.http import JsonResponse
def index(request):
    persons = ['张三','李四','王五']
    return HttpResponse(persons)
```

以上代码会报错，应该在使用`HttpResponse`的时候，传入一个`safe=False`参数，示例代码如下：

```python
return HttpResponse(persons,safe=False)
```



## 生成csv文件  

```python
from django.http import HttpResponse

import csv

def index(request):
    #第一步 告诉浏览器这是一个csv文件 不再是html文件
    response = HttpResponse(content_type='text/csv')
    #也就是告诉浏览器这是个附件 可以点击就会下载
    #添加一个Content-Disposition头
    #attachment 意思是 指明是个附件
    #文件的名字是: filename
    response['Content-Disposition'] = 'attachment;filename="kangbazi.csv"'
    #csv的writer方法 将相应的数据写入到 response 对象中
    writer =csv.writer(response)
    #一个writerow 代表一个数据行
    writer.writerow(['username','age','height','weight'])
    writer.writerow(['zhudaobuluke','18','190cm','180'])
    return response
```

* csv定义成模板 
* 大数据csv下载  
* 类视图 
* 错误定制 
* 表单  
* 文件上传

### csv 定义成模板  

> 利用django 自带的模板系统 给模板传入一个Context对象 ，然后生成 具体的csv文件  

```python
def template_csv_view(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment;filename=template.csv'
    context = {
        'rows':[
            ['username','age','height','weight'],
            ['陶总','20','190cm','90kg'],
        ]
    }  #准备context对象
    template = loader.get_template('index.txt') #加载模板文件 
    csv_template = template.render(context) #向模板传入context对象   
    response.content = csv_template 然后返回给浏览器    
    return response

index.txt  

	{% for row in rows %}{{ row.0 }},{{ row.1 }},{{ row.2 }},{{ row.3 }}
	{% endfor %}  
 	
    模板中可以使用过滤器   
```



### 生成大的csv文件  

> StreamingHttpResponse 是作为流返回给客户端 不是 返回一个整体   
>
> 好比视频 每分钟推部分流数据 而不是视频加载完了以后再推给客户端  
>
> 启动一个进程 用来跟 客户端 保持一个长连接 所以很耗资源 没有特殊的需求 尽量不启用  

```python
#一个整体的方式返回  
def large_csv_view(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment;filename=large.csv'
    writer = csv.writer(response)
    for row in range(1000000):
        writer.writerow(['Row {}'.format(row),'{}'.format(row)])
    return response

response = StreamingHttpResponse(content_type='text/csv')
response['Content-Disposition'] = 'attachment;filename=large.csv'
rows = ('Row {},{}\n'.format(row,row) for row in range(0,1000000))
response.streaming_content = rows  #流数据 

StreamingHttpResponse 这个类没有 content 属性 而是 streaming_content 是一个可迭代的对象   

这个类没有像HttpResponse 一样的 write方法 如果写入数据肯定会报错 

可以定义一个写操作的类 

class  Echo:
    def write(self,value):
        return value  
    
#如果执行csv.writer（） 的时候可以调用这个方法  
```



## 类视图  

```python
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
    def get(self,request,book_id,*args,**kwargs):    #传参数   
        print('图书的id是:%s' % book_id)
        return HttpResponse("成功")
    def dispatch(self, request, *args, **kwargs):  #get post put patch delete 任何请求都会走这个方法  
        print('不管你是什么方法都要走我这里')
        return super(BookDetailView, self).dispatch(request,*args,**kwargs)
    #跟flask 中的  dispatch_request一个道理
    #如果请求不被允许 那么走下面的方法  
    def http_method_not_allowed(self, request, *args, **kwargs):
        return HttpResponse('不支持get以外其他的请求'）
```

### TemplateView

>  专门用来渲染模板  

```
1.url.py    不需要写类视图  直接将模板映射到浏览器
from django.views.generic import TemplateView
urlpatterns = [
  	...
    path('about/',TemplateView.as_view(template_name='about.html'))
]

2.如果模板有动态变量   

views.py 

class AboutView(TemplateView):

    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = {"phone":"18888888888"}
        return context
        
 urls.py 
 	 path('about/',views.AboutView.as_view(),name="about")
```



### ListView 

> 我们经常需要展示列表  图书 文章等 ListView  能够帮助我们快速实现需求  

```python
class ArticleListView(ListView):
    model = Article #指定模型
    template_name = 'article_list.html' #模板
    context_object_name = 'articles' #渲染到模板上的对象
    paginate_by = 10 #每页展示多少条数据
    ordering = 'create_time' #列表的排序方式
    #127.0.0.1:9000/article/add/?page=1 page页码参数
    page_kwarg = 'page' #url参数 传递用户需求 想看第几页

    #获取上下文数据 简言之就是数据库中的数据
    def get_context_data(self,**kwargs):
        context = super(ArticleListView, self).get_context_data(**kwargs)
        return context

    #如果不想让所有的数据都返回那么我们可以重写一个方法将不需要的数据过滤掉

    def get_queryset(self):
        return Article.objects.filter(id__lte=50)
```

### Paginator、Page类 

* Paginator
  * 常用的属性和方法 
    * count: 总共有多少条数据
    * num_pages:总共有多少页
    * page_range页面的区间 比如有三页   range(1,4)
* Page
  * has_next 是否还有下一页
  * has_previous 是否还有上一页 
  * next_page_number:下一页的页码 
  * previous_page_number:上一页的页码
  * number:当前页 
  * start_index：当前这一页第一条数据的索引值
  * end_index:当前这一页最后一条数据的索引值

```python
views.py

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

```



index.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <!-- 最新版本的 Bootstrap 核心 CSS 文件 -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@3.3.7/dist/css/bootstrap.min.css"
          integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
</head>
<body>

<ul>
    {% for article in articles %}
        <li>{{ article.title }}</li>
    {% endfor %}
    <ul class="pagination">
        {#        上一页#}
        {% if page_obj.has_previous %}
            <li>
                <a href="{% url 'front:list' %}?page={{ page_obj.previous_page_number }}" aria-label="Previous">
                    <span aria-hidden="true">&laquo;</span>
                </a>
            </li>
        {% else %}
            <li class="disabled">
                <a href="javascript:void(0)" aria-label="Previous">
                    <span aria-hidden="true">&laquo;</span>
                </a>
            </li>
        {% endif %}
    {% if left_has_more %}
        <li><a href="{% url 'front:list' %}?page=1">1</a></li>
        <li><a href="javascript:void(0)">...</a></li>
    {% endif %}
    
{#       左边的页码#}
    {% for left_page in left_pages %}
         <li><a href="{% url 'front:list' %}?page={{ left_page }}">{{ left_page }}</a></li>
    {% endfor %}

    
{#    当前的页码 #}
     <li class="active"><a href="{% url 'front:list' %}?page={{ current_page }}">{{ current_page }}</a></li>
{#    右边的页码#}
    {% for right_page in right_pages %}
         <li><a href="{% url 'front:list' %}?page={{ right_page }}">{{ right_page }}</a></li>
    {% endfor %}


    {% if right_has_more %}
        <li><a href="javascript:void(0)">...</a></li>
        <li><a href="{% url 'front:list' %}?page={{ num_pages }}">{{ num_pages }}</a></li>
    {% endif %}


        {#        下一页 #}
        {% if page_obj.has_next %}
            <li>
                <a href="{% url 'front:list' %}?page={{ page_obj.next_page_number }}" aria-label="Previous">
                    <span aria-hidden="true">&raquo;</span>
                </a>
            </li>
        {% else %}
            <li class="disabled">
                <a href="javascript:void(0)" aria-label="Previous">
                    <span aria-hidden="true">&raquo;</span>
                </a>
            </li>
        {% endif %}
    </ul>
</ul>

</body>
</html>
```







## 明天计划 

* 类视图添加装饰器 
* 表单 
  * 文件上传  
* 会话控制  
* 上下文 和中间件  