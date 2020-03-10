import requests
import json
headers = {
    'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:64.0) Gecko/20100101 Firefox/64.0"
}

url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
#_o要去掉
f = input('请输入要翻译的内容:')

#en zh-CHS AUTO
data = {
    "i":f,
    "version":"2.1",
    "ts":"1583828597456",
    "to":" zh-CHS",
    "from":"AUTO",
    "smartresult":"AUTO",
    "client":"fanyideskweb",
    "salt":"15838292461802",
    "sign":"d179ebf9e387480bbed0e48c163147e0",
    "bv":"a9c3483a52d7863608142cc3f302a0ba",
    "doctype":"json",
    "keyfrom":"fanyi.web",
    "action":"FY_BY_CLICKBUTTION",
}

res = requests.post(url,data=data,headers=headers)
# print(res.text)

# dic = json.loads(res.text)
dic = res.json()

tgt = dic['translateResult'][0][0]['tgt']
print(tgt)