import requests

#GET 请求
response = requests.get('https://www.baidu.com')
print(response) #Response对象
print(response.status_code) #状态码 200
print(response.url) # 请求url地址https://www.baidu.com/
print(response.encoding) #编码类型ISO-8859-1
print(response.cookies) #cookie信息<RequestsCookieJar[<Cookie BDORZ=27315 for .baidu.com/>]>


#get 携带参数
headers = {
    "User-Agent":"Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
}
url = 'https://www.douban.com'
params = {
    'wd':'岛国电影'
}
response = requests.get(url=url,headers=headers,params=params)

# print(response.text) #返回的是Unicode格式的数据 根据自己的猜测解码
print(response.content.decode('utf-8')) #返回的是字节流数据 需要手动解码
print(response.cookies)