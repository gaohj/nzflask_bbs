"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path,include

urlpatterns = [
    path('account/', include('apps.qfauth.urls')), #认证地址
    path('cms/', include('apps.cms.urls')), #管理后台
    path('news/', include('apps.news.urls')), #前台
    path('ueditor/', include('apps.ueditor.urls')), #ueditor
]
