#encoding: utf-8

from django.urls import path
from . import views

app_name = 'course'

urlpatterns = [
    path('course_token/',views.course_token,name='course_token'),
]