from urllib import request
url = 'http://www.httpbin.org/ip'
res = request.urlopen(url)
print(res.read().decode('utf-8'))



url1 = 'http://www.httpbin.org/ip'
#构建处理器
handler = request.ProxyHandler({'https':'221.224.136.211:35101'})
#创建打开器
opener = request.build_opener(handler)
#构建请求对象
req1 = request.Request(url)
#使用打开器 发送请求
res1 = opener.open(req1)
print(res1.read().decode('utf-8'))
