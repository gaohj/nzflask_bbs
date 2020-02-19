from django.shortcuts import render

def index(request):
    context = {
        'persons':[
            '张三',
            '李四',
            '王五',
            '赵六'
        ]
    }
    return render(request,'index.html',context=context)