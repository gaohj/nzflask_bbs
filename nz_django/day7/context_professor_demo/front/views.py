from django.shortcuts import render
from .models import User
# Create your views here.
def index(request):
    # users = []
    # for x in range(0,51):
    #     user = User(username='用户名:%s'%x,password='password:%s'% x,telephone='138123456:%s'%x)
    #     users.append(user)
    # User.objects.bulk_create(users)
    users = User.objects.all()
    context = {
        'users':users
    }
    return render(request,'index.html',context=context)