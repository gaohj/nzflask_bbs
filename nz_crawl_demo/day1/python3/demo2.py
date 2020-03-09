#encoding:utf-8
# import sys
# print sys.version  打印python的版本

import urllib.parse
from urllib import request
def baidu(params):
    url = "https://www.baidu.com/s?" + params

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",
    }

    request = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(request)
    #bytes => str  decode
    #str => bytes  encode
    print(response.read().decode('utf-8'))

if __name__ == "__main__":

    #https://www.baidu.com/s?wd=%E8%8B%8D%E8%80%81%E5%B8%88&chrome=utf-8
    #用户想要查询的关键词
    kw = input("请输入要搜索的内容")
    params = {'wd':kw,'chrome':'utf-8'}
    #将字典拼接成 url

    #urllib 没有urlencode 需要通过 parse对象 方法
    params = urllib.parse.urlencode(params)
    print(params)

    baidu(params)


