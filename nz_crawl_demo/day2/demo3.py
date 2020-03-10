from urllib import request
from urllib import parse
import json
headers = {
    "User-Agent":"Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
}

url = "https://music.163.com/weapi/v1/resource/comments/A_PL_0_924680166?csrf_token=6789630a244c9d7be267d088f0bbe1d7"


data = {
    "params":"mHGCIYkOHJX/oh5U406M1WxDG2PLmsITXpiO72w/OAcQcDCbgnPdPKQAklWewgUSUvwnI4jUOB+MAya+TP7elRexKUl0+qh0eZpPTCn0GfyvqsrGMIESAia2vK2BvkaQWo8IcKLZ6rLpMeUwmYs7T7/kmSJ+W0KZYk+G9rA49hnL1HO3xk7XqQcsTr7SUD7oQg8GjUs4tF8n90aLorGXpLLYY65XGM9XtncQAbfvnSo=",
    "encSecKey":"31d89f28b1878d7935c4e5c0416438d542102e90273669d2206c837427f2313e1cbf26af2572b736e2adee43bb284bd767e2fd7ce6c9e3a0540f04bd2f863e682c8fa9d46d7e082955de3e66a14649b1bbec6f7f8fab026cc473f116c99c88cf3704ead5763fb565f41a4201f6127d736e0f31bbf68918f69cde49111f411aa0"
}

#将参数进行url编码  变成浏览器是别的
#urlencode 如果url 中 有中文及特殊字符 自动的进行编码
#如果我们使用代码发送请求  那么必须手动进行编码
#用 urlib.parse.urlencode
data  = parse.urlencode(data).encode()
#decode 是 由 bytes类型 => str类型
#encode 是 str类型 => bytes类型
# print(data)

req = request.Request(url,headers=headers,data=data) #传入二进制参数

res = request.urlopen(req)
# print(res.read().decode('utf-8'))
content = res.read().decode('utf-8')

#解析json
data_dict = json.loads(content)
# print(data_dict)

hotComments = data_dict['hotComments']
for hotComment in hotComments:
    nickname = hotComment['user']['nickname']
    content = hotComment['content']
    print(nickname,":",content)