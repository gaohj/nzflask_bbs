import requests

headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",
        "Upgrade-Insecure-Requests":'1',
    }

url = "http://www.doutula.com/photo/list/?page=2"

ip_list = [
    {'http':"110.243.15.248:9999"},
]

import random
proxy = random.choice(ip_list)
res = requests.get(url,headers=headers)
print(res.text)