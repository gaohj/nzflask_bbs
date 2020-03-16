import requests
import re
from urllib import request
from fontTools.ttLib import TTFont
def get_doutin():
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",
    }
    url = "https://www.iesdouyin.com/share/user/88445518961"
    res = requests.get(url,headers=headers,verify=False)
    html = res.text
    # font_url = "http://s3.pstatp.com/ies/resource/falcon/douyin_falcon/static/font/iconfont_9eb9a50.woff"
    #     # request.urlretrieve(font_url,'testt.woff')
    return html

# def analysis_font():
#     baseFont = TTFont('testt.woff')
#     baseFont.saveXML('douyin.xml')

def get_real_word(content):
    #网页上显示的 是 &#xe603; 处理成 Oxe603
    content = content.replace('&#','0').replace(';','')
    print(content)
    #预先定义好 它们的映射关系 name最终文字
    name_word_list = [
        {"name":['0xe603','0xe60d','0xe616'],'value':'0'},
        {"name":['0xe602','0xe60e','0xe618'],'value':'1'},
        {"name":['0xe605','0xe617','0xe610'],'value':'2'},
        {"name":['0xe604','0xe611','0xe61a'],'value':'3'},
        {"name":['0xe606','0xe60c','0xe619'],'value':'4'},
        {"name":['0xe607','0xe60f','0xe61b'],'value':'5'},
        {"name":['0xe612','0xe608','0xe61f'],'value':'6'},
        {"name":['0xe613','0xe60a','0xe61c'],'value':'7'},
        {"name":['0xe60b','0xe614','0xe61d'],'value':'8'},
        {"name":['0xe609','0xe615','0xe61e'],'value':'9'},
    ]

    for name_word in name_word_list:
        for font_code in  name_word['name']:
            content = re.sub(font_code,name_word['value'],content)
    print(content)

if __name__ == "__main__":
    content  = get_doutin()
    info = get_real_word(content)
