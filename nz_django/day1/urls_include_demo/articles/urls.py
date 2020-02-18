from django.urls import re_path
from . import views


urlpatterns = [
    #r'' 表示原生字符串
    re_path(r'^$',views.index),
    re_path(r'^list/(?P<year>\d{4})/$',views.article_list),
    re_path(r'^author/(?P<tels>1[3-9]\d{9})/$',views.author_tel),
]