from django.http import HttpResponse,StreamingHttpResponse
from django.template import loader
import csv

def index(request):
    #第一步 告诉浏览器这是一个csv文件 不再是html文件
    response = HttpResponse(content_type='text/csv')
    # response.content = '我是返回给浏览器的内容'
    # response.write('我写到content中')
    #也就是告诉浏览器这是个附件 可以点击就会下载
    #添加一个Content-Disposition头
    #attachment 意思是 指明是个附件
    #文件的名字是: filename
    response['Content-Disposition'] = 'attachment;filename="kangbazi.csv"'
    #csv的writer方法 将相应的数据写入到 response 对象中
    writer =csv.writer(response)
    #一个writerow 代表一个数据行
    writer.writerow(['username','age','height','weight'])
    writer.writerow(['zhudaobuluke','18','190cm','180'])
    return response

def template_csv_view(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment;filename=template.csv'
    context = {
        'rows':[
            ['username','age','height','weight'],
            ['陶总','20','190cm','90kg'],
        ]
    }
    template = loader.get_template('index.txt')
    csv_template = template.render(context)
    response.content = csv_template
    return response

def large_csv_view(request):
    # response = HttpResponse(content_type='text/csv')
    # response['Content-Disposition'] = 'attachment;filename=large.csv'
    # writer = csv.writer(response)
    # for row in range(1000000):
    #     writer.writerow(['Row {}'.format(row),'{}'.format(row)])
    response = StreamingHttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment;filename=large.csv'
    rows = ('Row {},{}\n'.format(row,row) for row in range(0,1000000))
    response.streaming_content = rows
    return response