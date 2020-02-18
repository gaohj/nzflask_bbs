"""urls_include_demo URL Configuration

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
from django.urls import path,include
from movie import views as movie
from music import views as music
#http://www.douban.com/book/list
#http://www.douban.com/movie/list
urlpatterns = [
    path('book/',include('book.urls')),
    path('articles/',include('articles.urls')),
    path('movie/',include([
        path('',movie.index),
        path('detail/<movie_id>/',movie.movie_detail)
    ])),
    path('music/',include([
        path('',music.index),
        path('detail/<music_id>/',music.music_detail)
    ])),

]
