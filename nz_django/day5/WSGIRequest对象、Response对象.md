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