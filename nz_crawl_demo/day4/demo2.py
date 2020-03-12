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
def main(startUrl):
    #用列表 模拟队列
    url_queue = []
    url_queue.append(startUrl)
    while len(url_queue) > 0:
        url = url_queue.pop(0)  # 每次取出列表第一个
        print("\t" * deep_dict[url], "当前层级:%d" % deep_dict[url])
        if deep_dict[url] < 4:
            sonList = get_son_url(url)  # 获取子url列表
            for son_url in sonList:
                # 过滤有效的url
                if son_url.startswith('http') or son_url.startswith('https'):
                    if son_url not in deep_dict:  # 过滤重复url
                        deep_dict[son_url] = deep_dict[url] + 1  # 层级加1
                        url_queue.append(son_url)  # 将子url进入队列
if __name__ == "__main__":
    url = "https://www.so.com/s?q=%E5%B2%9B%E5%9B%BD%E7%A7%8D%E5%AD%90"
    deep_dict = {}
    deep_dict[url] = 1 #默认层级为1
    main(url)

