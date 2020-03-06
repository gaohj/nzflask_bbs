# 单元测试工具 django-debug-toolbar  

> https://django-debug-toolbar.readthedocs.io/en/latest/configuration.html
>
> 官方手册



## 安装 

```
pip install django-debug-toolbar
```



## 配置

```
    # ...
    'django.contrib.staticfiles',
    # ...
    'debug_toolbar',
]

STATIC_URL = '/static/'
```



## url配置 

```
from django.urls import path,include
from django.conf import settings
urlpatterns = [
    ...
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns.append( path('__debug__/', include(debug_toolbar.urls))),

```

## 中间件

```
MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
   ...
]
```

## 额外配置 

```python
INTERNAL_IPS = ['127.0.0.1']

DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel', #哪个django版本
    'debug_toolbar.panels.timer.TimerPanel', #加载当前页面 花费了多长时间 
    'debug_toolbar.panels.settings.SettingsPanel',#读取该项目django的配置信息
    'debug_toolbar.panels.headers.HeadersPanel',#查看请求头信息
    'debug_toolbar.panels.request.RequestPanel',#请求的信息  视图函数cookie session等
    'debug_toolbar.panels.sql.SQLPanel', #执行了哪些sql语句 才获取当前的数据
    'debug_toolbar.panels.staticfiles.StaticFilesPanel', #静态文件
    'debug_toolbar.panels.templates.TemplatesPanel', #模板文件
    'debug_toolbar.panels.cache.CachePanel', #缓存
    'debug_toolbar.panels.signals.SignalsPanel',#信号
    'debug_toolbar.panels.logging.LoggingPanel', #日志
    'debug_toolbar.panels.redirects.RedirectsPanel',#重定向
    'debug_toolbar.panels.profiling.ProfilingPanel',
]
```



## 通过命令 来实现  分组 及权限 

> https://docs.djangoproject.com/en/2.0/howto/custom-management-commands/ 

### 创建python包 

```
polls/
    __init__.py
    models.py
    management/
        __init__.py
        commands/
            __init__.py
            init_group.py
            
init_group.py

from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('初始化成功')
        
python manage.py init_group #运行这个命令即可
```

