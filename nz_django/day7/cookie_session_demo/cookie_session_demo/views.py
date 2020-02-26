from django.http import HttpResponse
from datetime import datetime
from django.utils.timezone import make_aware

def index(request):
    response = HttpResponse('index')
    expires = datetime(year=2020,month=2,day=28,hour=2,minute=2,second=30)
    expires = make_aware(expires)
    response.set_cookie('user_id','kangbazi',max_age=1800,expires=expires)
    return response
def delete_view(request): #删除cookie也是用response对象
    response = HttpResponse('delete')
    response.delete_cookie('user_id')
    return response

def get_view(request):
    cookies = request.COOKIES #获取cookie用的request对象
    username = cookies.get('user_id')
    return HttpResponse(username)

def cms_view(request):
    cookies = request.COOKIES #获取cookie用的request对象
    username = cookies.get('user_id')
    return HttpResponse(username)
from datetime import timedelta
def session_view(request):
    request.session['username'] = 'kangbazi'
    # expiry = timedelta(days=2)
    request.session.set_expiry(3600) #只支持 整型 0  None
    return HttpResponse('session_view')

def get_session_view(request):
    username = request.session.get('username')
    return HttpResponse(username)
# import django.contrib.sessions.backends.file