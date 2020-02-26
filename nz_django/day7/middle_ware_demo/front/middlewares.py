#获取登录用户的详细信息
from .models import User

#get_response是一个方法
def front_user_middleware(get_response):
    #执行一些初始化的代码
    print("在这里执行一些中间件初始化的代码")
    def middleware(request): #真正的执行在这里
        print('这里执行的是request到达view之前的代码')
        user_id = request.session.get('user_id')
        if user_id:
            try:
                user = User.objects.get(pk=user_id)
                request.front_user = user
            except:
                request.front_user = None
        else:
            request.front_user = None
        response  = get_response(request) #以这个为界限
        print('下面就是response到达浏览器之前的代码')
        return response
    return middleware

class FrontUserMiddleware(object):
    def __init__(self,get_response):
        #在这里执行一些初始化的代码
        print('类中间件初始化的代码')
        self.get_response = get_response
    def __call__(self,request):#为每个请求响应执行的代码
        print('类request到达view之前执行的代码')
        user_id = request.session.get('user_id')
        if user_id:
            try:
                user = User.objects.get(pk=user_id)
                request.front_user = user
            except:
                request.front_user = None
        else:
            request.front_user = None

        response = self.get_response(request) #以这个为界限
        print('类response到达浏览器之前执行的代码')
        return response

from django.utils.deprecation import MiddlewareMixin
class FrontUserMiddlewareMixin(MiddlewareMixin):
    def __init__(self,get_response):
        #执行初始化的代码
        super(FrontUserMiddlewareMixin, self).__init__(get_response)
    #request到达view之前
    def process_request(self,request):
        print('类request到达view之前执行的代码')
        user_id = request.session.get('user_id')
        if user_id:
            try:
                user = User.objects.get(pk=user_id)
                request.front_user = user
            except:
                request.front_user = None
        else:
            request.front_user = None
    #response到达浏览器之前
    def process_response(self,request,response):
        print('这里处理的是response到达浏览器之前的代码')
        return response