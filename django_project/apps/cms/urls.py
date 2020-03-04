from django.urls import path
from . import views

app_name = 'cms'

urlpatterns = [
    path('',views.index,name='index'),
    path('add_news_category/',views.add_news_category,name='add_news_category'),
    path('news_category/',views.news_category,name='news_category'),
    path('write_news/',views.WriteNewsView.as_view(),name='write_news'),
    path('qntoken/',views.qiniu_token,name='qntoken')
]