import requests
import random
from chaojiying import Chaojiying_Client
ua_list= [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
    "Opera/9.80 (X11; Linux i686; Ubuntu/14.10) Presto/2.12.388 Version/12.16",
    "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:63.0) Gecko/20100101 Firefox/63.0",
]

ua = random.choice(ua_list)
headers = {
    'User-Agent':ua
}


def login(code):
    url = "http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=2020251654233"
    data = {
        'icode':code,
        'email':'gaohj5@163.com',
        'password':'12qwaszx',
        'origURL':'http://www.renren.com/541197383',
        'domain':'renren.com',
        'key_id':'1',
        'captcha_type':'web_login',
        'f':''
    }

    res = session.post(url,headers=headers,data=data)

    #获取结果
    res = res.content.decode()
    print(res)

def get_code():
    url = "http://icode.renren.com/getcode.do?t=web_login&rnd=%s" % (random.random())

    res = session.get(url,headers=headers)

    #保存图片
    with open('code.jpg','wb') as fp:
        fp.write(res.content)
        fp.flush()

    chaojiying = Chaojiying_Client('gaohj5', '12qwaszx', '903943')  # 用户中心>>软件ID 生成一个替换 96001
    im = open('code.jpg', 'rb').read()  # 本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
    result = chaojiying.PostPic(im, 1902)['pic_str']
    return result

def get_profile():
    url = "http://www.renren.com/541197383/profile"
    res = session.get(url,headers=headers)
    result = res.content.decode()
    print(result)
if __name__ == "__main__":
    session = requests.session()
    code = get_code()
    login(code)
    get_profile()
