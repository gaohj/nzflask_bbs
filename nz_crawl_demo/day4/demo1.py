#encoding:utf-8
import re
import requests
#深度爬取 递归
from lxml import etree

headers = {
    "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
}


def getHTML(url):
    try:
        res = requests.get(url,headers=headers)
        # print(res.content.decode('utf-8'))
        return res.content.decode('utf-8')
    except:
        return ""

def get_son_url(url):

    text = getHTML(url) #获取页面内容
    html = etree.HTML(text)
    #规则
    aList = html.xpath("//a/@href")
    return aList
def main(url):
    if deep_dict[url] > 4:
        return
    print("\t" * deep_dict[url],"当前层级:%d" % deep_dict[url])
    #获取网页子url
    sonurl_list = get_son_url(url)
    for sonurl in sonurl_list:
        #过滤有效链接
        if sonurl.startswith('http') or sonurl.startswith('https'):
            if sonurl not in deep_dict:#过滤重复的url
                deep_dict[sonurl] = deep_dict[url] + 1
                main(sonurl) #递归爬取子url
if __name__ == "__main__":
    url = "https://www.so.com/s?q=%E5%B2%9B%E5%9B%BD%E7%A7%8D%E5%AD%90"
    deep_dict = {}
    deep_dict[url] = 1 #默认层级为1
    main(url)

