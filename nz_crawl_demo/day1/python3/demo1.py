#encoding:utf-8
# import sys
# print sys.version  打印python的版本

import urllib
from urllib import request
url = "https://www.baidu.com"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",
}

#构建请求对象
request = urllib.request.Request(url,headers=headers)
res = urllib.request.urlopen(request)
# print(res.read()) #二进制形式的
# print(res.read().decode('utf-8')) #转成字符串
print(res.info()) #响应的信息
