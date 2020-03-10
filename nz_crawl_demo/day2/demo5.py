from urllib import parse

params = {'name':'张三','age':18,'greet':'hello world'}
qs = parse.urlencode(params)
print(qs) #name=%E5%BC%A0%E4%B8%89&age=18&greet=hello+world

res =parse.parse_qs(qs)
# print(res) #name=%E5%BC%A0%E4%B8%89&age=18&greet=hello+world

# https://www.baidu.com/s?wd=朱道布鲁克&rsv_spt=1&rsv_iqid=0
url = "https://www.baidu.com/s?wd=朱道布鲁克&rsv_spt=1&rsv_iqid=0"
result = parse.urlparse(url=url)
print(result)

result1 = parse.urlsplit(url=url)
#split
print(result1)
print(result1.query)
print(result1.netloc)
