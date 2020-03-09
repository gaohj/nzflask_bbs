#encoding:utf-8
# import sys
# print sys.version  打印python的版本

import urllib2
url = "https://www.baidu.com"
response = urllib2.urlopen(url)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",
}

#创建请求对象

request = urllib2.Request(url=url,headers=headers)

#请求对象可以做以下事情
print request.get_full_url()#https://www.baidu.com
print request.get_method() #GET
print request.get_host() #www.baidu.com
print request.get_type() #https
print request.get_header('User-Agent')


request.add_header('Connection','keep-Alive') #添加head头 
print request.get_header('Connection')
#发送请求得到响应
response = urllib2.urlopen(request)
# print response.code
# print response.read() #得到网页的源代码

