import uuid
from django.core.cache import cache
from rest_framework import viewsets,status
from .models import Book,Game,Movie,User
from rest_framework.response import Response
from rest_framework.exceptions import APIException,NotFound
from .serializers import BookSerializer,Book2Serializer,Book3Serializer,GameSerializer,MovieSerializer,UserSerializer
from rest_framework.generics import CreateAPIView,ListAPIView,ListCreateAPIView,RetrieveAPIView,UpdateAPIView
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = Book3Serializer


#TemplateView  ListView
# class GameCreatAPIView(CreateAPIView): #只能post请求
#     queryset = Game
#     serializer_class = GameSerializer

# class GameCreatAPIView(ListAPIView): #只能get请求
#     queryset = Game.objects.all()
#     serializer_class = GameSerializer

# class GameCreatAPIView(ListCreateAPIView): #只能get和post请求
#     queryset = Game.objects.all()
#     serializer_class = GameSerializer

#url =    re_path(r'games/(?P<pk>\d+)/',views.GameCreatAPIView.as_view(),name='create_game'),

class GameCreatAPIView(RetrieveAPIView): #只能get和post请求
    queryset = Game.objects.all()
    serializer_class = GameSerializer

from .authentications import UserAuthentication
from .permissions import UserLoginPermission
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    authentication_classes = UserAuthentication,
    permission_classes = UserLoginPermission,

class UserCreateApiView(CreateAPIView):#只能post请求
    serializer_class = UserSerializer
    def post(self, request, *args, **kwargs):
        action = request.GET.get('action')
        #http://127.0.0.1:8088/view/users/?action=register
        if action == 'register':
            return self.create(request,*args, **kwargs)
        #http://127.0.0.1:8088/view/users/?action=login
        elif action == 'login':
            return self.do_login(request,*args, **kwargs)
        else:
            raise APIException(detail='只能登录或者注册')
    def do_login(self,request,*args, **kwargs):
        #接收字段
        # u_name = request.POST.get('u_name')
        u_name = request.data.get('u_name')
        m_password = request.POST.get('m_password')
        try:
            user = User.objects.get(u_name=u_name)
        except User.DoesNotExist as e:
            raise NotFound(detail='该用户不存在')

        if user.m_password != m_password:
            raise APIException(detail='密码有误请重新输入')

        #登录成功以后 我们要求必须生成token

        token = uuid.uuid4().hex

        #生成token同时 将其存入缓存中
        cache.set(token,user.id,timeout=60*60*24*7)

        data = {
            'status':status.HTTP_200_OK,
            'msg':"登录成功",
            'token':token
        }
        return Response(data)


