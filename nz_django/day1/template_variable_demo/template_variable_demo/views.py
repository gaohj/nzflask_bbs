from django.shortcuts import render
class Person(object):
    def __init__(self,username):
        self.username = username

def index(request):
    # p = Person('wh_kangbazi')
    # context = {
    #     'person':p
    # }
    # context = {
    #     'person':{
    #         'username':'kangbazi',
    #         'password':'123456'
    #     } #返回字典的时候
    # }
    context = {
        'persons':(
            '刘键',
            '志远',
            '本胜'
        )
    }
    return render(request,'index.html',context=context)
