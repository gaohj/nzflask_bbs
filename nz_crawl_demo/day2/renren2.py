from http.cookiejar import CookieJar,FileCookieJar,MozillaCookieJar,LWPCookieJar
from urllib import parse
from urllib import request
headers = {
    "User-Agent":"Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
}
#创建打开器
def get_opener():
    cookiejar = CookieJar()
    handler = request.HTTPCookieProcessor(cookiejar) #存储cookie信息
    opener = request.build_opener(handler) #携带cookie信息发送请求
    return opener

#登录人人网
def login_renren(opener):
    data = {
        "email":'gaohj5@163.com',
        "password":'12qwaszx',
    }
    data = parse.urlencode(data).encode('utf-8')
    url = "http://www.renren.com/PLogin.do"
    req = request.Request(url=url,headers=headers,data=data)
    opener.open(req)


#访问个人中心  并下载
def visit_profile(opener):
    url = "http://www.renren.com/541197383/profile"
    req = request.Request(url,headers=headers)
    res = opener.open(req)
    with open('renren2.html', 'w', encoding='utf-8') as fp:
        fp.write(res.read().decode('utf-8'))


if __name__ == "__main__":
    opener = get_opener()
    login_renren(opener)
    visit_profile(opener)

