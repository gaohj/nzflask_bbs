import os
import requests #请求库
from  urllib import request # 下载图片用
from lxml import etree  #网络解析库
from queue import Queue #队列
import threading
import re
import csv
#生产者  页面队列取出  然后下载页面中的 图片url  放入图片队列
class Producer(threading.Thread):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",
        "Upgrade-Insecure-Requests":'1',
    }
    def __init__(self,page_queue,joke_queue,*args,**kwargs):
        super(Producer, self).__init__(*args,**kwargs)
        self.base_domain = 'http://www.budejie.com'
        self.page_queue = page_queue
        self.joke_queue = joke_queue

    def run(self):
        while True:
            if self.page_queue.empty():
                break
            url = self.page_queue.get()
            self.parse_page(url)
    def parse_page(self,url):
        response = requests.get(url,headers=self.headers)
        text = response.text
        html = etree.HTML(text)
        descs = html.xpath("//div[@class='j-r-list-c-desc']")
        for desc in descs:
           jokes = desc.xpath(".//text()")
           joke = "\n".join(jokes).strip()
           link = self.base_domain+desc.xpath(".//a/@href")[0]
           self.joke_queue.put((joke,link))
           print("="*30+"第%s页面下载完成"%url.split('/')[-1]+"="*30)
#消费者  图片队列中取出 然后进行下载
class Consumer(threading.Thread):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
    }

    def __init__(self, joke_queue,writer,gLock,*args, **kwargs):
        super(Consumer, self).__init__(*args, **kwargs)
        self.joke_queue = joke_queue
        self.writer = writer
        self.gLock = gLock


    def run(self):
        #从图片队列中取出 图片的url 然后进行下载
        while True:
            try:
                joke_info = self.joke_queue.get(timeout=30)
                joke,link = joke_info
                self.gLock.acquire()
                self.writer.writerow((joke,link))
                self.gLock.release()
                print('保存一条成功')
            except:
                break



def main():
    #页面的队列
    page_queue = Queue(88)
    #存放图片
    joke_queue = Queue(998)
    gLock = threading.Lock()
    fp = open('bsbdj.csv','a',newline='',encoding='utf-8')
    writer = csv.writer(fp)
    writer.writerow(('content','link'))

    for x in range(1,89):
        url = "http://www.budejie.com/text/%d" % x
        page_queue.put(url)

    for x in range(5):
        t = Producer(page_queue,joke_queue)
        t.start()

    for x in range(5):
        t = Consumer(joke_queue,writer,gLock)
        t.start()

if __name__ == "__main__":
    main()