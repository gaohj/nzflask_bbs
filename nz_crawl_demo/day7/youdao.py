import random
import time
import requests
import hashlib


def generateSaltSign(e):
    navigator_appVersion = "5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
    t = hashlib.md5(navigator_appVersion.encode("utf-8")).hexdigest()
    r = str(int(time.time() * 1000))
    i = r + str(random.randint(1, 10))
    return {
        "ts": r,
        "bv": t,
        "salt": i,
        "sign": hashlib.md5(str("fanyideskweb" + e + i + "97_3(jkMYg@T[KZQmqjTK").encode("utf-8")).hexdigest()
    }


def spider(i):
    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    r = generateSaltSign(i)

    data = {
        "i": i,
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": r["salt"],
        "sign": r["sign"],
        "ts": r["ts"],
        "bv": r["bv"],
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_REALTlME",
    }
    # data = parse.urlencode(data).encode('utf-8')

    headers = {
        "Cookie": "OUTFOX_SEARCH_USER_ID=-286220249@10.108.160.17;",
        "Referer": "http://fanyi.youdao.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
    }
    response = requests.post(url=url, data=data, headers=headers)
    print(response.text)


if __name__ == '__main__':
    i = input("请输入你要查询的字符串:")
    spider(i)