import requests
auth = ('test','123456')
headers = {
    'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:64.0) Gecko/20100101 Firefox/64.0"
}
res = requests.get("https://api.github.com/user",headers=headers,verify=False,auth=auth)
print(res.text)


#encoding: utf-8
import requests

resp = requests.get('http://www.12306.cn/mormhweb/',verify=True)
with open('12306.html','w',encoding='utf-8') as fp:
    fp.write(resp.content.decode('utf-8'))