from urllib import request

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",
}

# req = request.Request(url="https://www.baidu.com",headers=headers)
# request.urlretrieve("http://www.renren.com","1.html")
url = 'https://www.baidu.com'
request.urlretrieve(url,'2.html')