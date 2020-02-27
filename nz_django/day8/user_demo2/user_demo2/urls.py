"""user_demo2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from front import views

urlpatterns = [
    path('',views.index,name='index'),
    path('proxy/',views.proxy_view,name='proxy'),
    path('add/',views.add_article,name='add'),
    path('group/',views.operate_group,name='group'),
    path('one/',views.one_view,name='one'),
    path('inherit/',views.inherit_view,name='inherit'),
    path('signin/',views.my_login,name='signin'),
    path('logout/',views.my_logout,name='logout'),
    path('profile/',views.profile,name='profile'),
    path('operate_permission/',views.operate_permission,name='operate_permission'),
    path('add_permission/',views.add_permission,name='add_permission'),

]
