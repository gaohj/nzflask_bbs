import requests
import json
import hashlib
import time
import random
headers = {
    'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:64.0) Gecko/20100101 Firefox/64.0",
    'Referer':'http://fanyi.youdao.com/',
    'Cookie':'OUTFOX_SEARCH_USER_ID=1261780805@10.108.160.18;'

}

def generateSaltSign(e):
    navigator_appVersion = "5.0 (Windows NT 6.1; WOW64; rv:64.0) Gecko/20100101 Firefox/64.0"
    t = hashlib.md5(navigator_appVersion.encode('utf-8')).hexdigest()
    r = str(int(time.time()*1000))
    i = r + str(random.randint(1,10))
    return {
        'ts':r,
        'bv':t,
        'salt':i,
        'sign':hashlib.md5(str("fanyideskweb" + e + i + "Nw(nmmbP%A-r6U3EUn]Aj").encode('utf-8')).hexdigest()

    }


url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
#_o要去掉

f = input('请输入要翻译的内容:')
res = generateSaltSign(f)
print(res)
#en zh-CHS AUTO
data = {
    "i":f, #需要翻译的字符串
    "version":"2.1", #版本固定值
    "ts":res['ts'], #时间戳 毫秒级别
    "to":" zh-CHS", #翻译后的语种
    "from":"AUTO", #源语言的语种
    "smartresult":"AUTO", #智能结果  固定值
    "client":"fanyideskweb",#客户端  固定值
    "salt":res['salt'], #加密用的盐  不固定
    "sign":res['sign'],#签名字符串 不固定
    "bv":res['bv'],#md5值 固定导入
    "doctype":"json",#文档类型
    "keyfrom":"fanyi.web", #键来源 固定值
    "action":"FY_BY_CLICKBUTTION",#操作动作  固定值
}

res = requests.post(url,data=data,headers=headers)
print(res.text)

# # dic = json.loads(res.text)
# dic = res.json()
#
# tgt = dic['translateResult'][0][0]['tgt']
# print(tgt)