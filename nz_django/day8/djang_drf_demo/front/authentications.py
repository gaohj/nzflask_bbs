from django.core.cache import cache
from rest_framework.authentication import BaseAuthentication
from .models import User
#首先根据token从缓存中取出来 没有返回空

#如果有 取出指定的 user.id
#根据user.id 从数据库中取出详细的信息
#判断是否有权限

class UserAuthentication(BaseAuthentication):
    def authenticate(self, request):
        try:
            token = request.GET.get('token')
            user_id = cache.get(token) #根据键 查出值

            user = User.objects.get(pk=user_id) #取出详细的信息
            return user,token
        except Exception as e:
            return None
