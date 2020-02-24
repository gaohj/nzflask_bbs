from django.http import HttpResponse

import csv

def index(request):
    #第一步 告诉浏览器这是一个csv文件 不再是html文件
    response = HttpResponse(content_type='text/csv')
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