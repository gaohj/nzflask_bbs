from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('detail/<int:book_id>/', views.book_detail,{'name':'kangbazi'}),
]
