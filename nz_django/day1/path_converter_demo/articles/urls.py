from django.urls import path,re_path
from . import views

urlpatterns = [
    path('',views.article,name='index'),
    # re_path(r'^list/(?P<categories>\w+|(\w+\+\w+)+)/$',views.article_list,name='list')
    path('list/<cate:categories>/',views.article_list,name='list'),
    path('detail/<int:article_id>/',views.article_detail,name='detail')
]