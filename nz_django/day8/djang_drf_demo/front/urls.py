from django.urls import path,re_path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

router.register(r'books',views.BookViewSet)

urlpatterns = [
    re_path(r'games/(?P<pk>\d+)/',views.GameCreatAPIView.as_view(),name='create_game'),
    #get post
    #http://127.0.0.1:8088/api/movies/
    re_path(r'^movies/$',views.MovieViewSet.as_view(actions={"get": "list","post": "create"})),
    #get http://127.0.0.1:8088/api/movies/1/
    #put  http://127.0.0.1:8088/api/movies/1/
    #patch http://127.0.0.1:8088/api/movies/1/
    #delete http://127.0.0.1:8088/api/movies/1/
    re_path(r'^movies/(?P<pk>\d+)/$', views.MovieViewSet.as_view(actions={"get": "retrieve"})),
    re_path(r'^users/',views.UserCreateApiView.as_view()),
]