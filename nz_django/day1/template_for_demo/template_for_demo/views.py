from django.shortcuts import render
def index(request):
    context = {
        'books':[
            '水浒传',
            '红楼梦',
            '金瓶梅',
            '明朝那些事',
            '三国演义'
        ],
        'persons':{
            'username':'朱道布鲁克',
            'age':18,
            'height':'201cm',
            'location':'得分后卫'
        },
        'bookses':[
            {
                'name':'自带电池的Python',
                'author':'头发最茂密的语言发明者',
                'price':200
            },
            {
                'name': 'mysql从删除到跑路',
                'author': '战斗渣',
                'price': 50
            },
            {
                'name': 'java从入门到放弃',
                'author': '老大哥',
                'price': 60
            },
            {
                'name': 'linux深入浅出',
                'author': '林纳斯',
                'price': 600
            },

        ],
        'commets':''
    }
    return render(request,'index.html',context=context)
