from django.urls import path
from . import views

app_name = 'errors'

urlpatterns = [
    path('403.html/',views.view_403,name='403'),
    path('404.html/',views.view_400,name='400'),
]