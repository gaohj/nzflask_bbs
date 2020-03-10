import requests
from urllib import request
url = "http://www.baidu.com"
headers = {
    'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:64.0) Gecko/20100101 Firefox/64.0"
}

res = requests.get(url,headers=headers)
print(res.status_code)
if res.status_code == 200:
    request.urlretrieve(url,'baidu.html')