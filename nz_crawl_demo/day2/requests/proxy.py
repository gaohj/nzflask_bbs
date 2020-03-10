import requests
import json

url = "http://www.httpbin.org/ip"
headers = {
    'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:64.0) Gecko/20100101 Firefox/64.0"
}
proxy = {
    'http':'58.22.204.55:9999'
}
res = requests.get(url=url,headers=headers,proxies=proxy)
print(res.text)

