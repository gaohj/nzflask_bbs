from django.conf.urls import url
from . import views

app_name = 'tasks'
urlpatterns = [
    url('do_task1/',views.do_task1,name='do_task1'),
    url('do_task2/',views.do_task2,name='do_task2'),

]