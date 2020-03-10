import requests

url = "http://www.renren.com/PLogin.do"
data = {
    "email":"gaohj5@163.com",
    "password":'12qwaszx',
}
headers = {
    'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:64.0) Gecko/20100101 Firefox/64.0"
}

#登录

session = requests.Session() #实例化一个session对象

session.post(url,data=data,headers=headers)

res = session.get("http://www.renren.com/541197383/profile")
with open('renren6.html','w',encoding='utf-8') as fp:
    fp.write(res.content.decode('utf-8'))


# http://www.xbiquge.la/login.php?jumpurl=http://www.xbiquge.la/