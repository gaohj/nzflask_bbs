#encoding:utf-8
# import sys
# print sys.version  打印python的版本

import urllib2
url = "https://www.baidu.com"
#urlopen 打开url 并且访问url
#参数1 url地址
#参数2  data 如果设置了 data 那么就认为你是post请求  不加就是get请求
#参数3  timeout 超时时间
response = urllib2.urlopen(url)

# print response #<addinfourl at 61235080L whose fp = <socket._fileobject object at 0x00000000037ABC00>>


# print response.read() #返回网页所有的数据
# print response.readline() #返回1行
print response.readlines() #读取所有的行
