import os
import requests #请求库
from  urllib import request # 下载图片用
from lxml import etree  #网络解析库
from queue import Queue #队列
import threading
import re
#生产者  页面队列取出  然后下载页面中的 图片url  放入图片队列
class Producer(threading.Thread):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",
        "Upgrade-Insecure-Requests":'1',
    }
    def __init__(self,page_queue,img_queue,*args,**kwargs):
        super(Producer, self).__init__(*args,**kwargs)
        self.page_queue = page_queue
        self.img_queue = img_queue

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
        imgs = html.xpath("//div[@class='page-content text-center']//a//img")
        for img in imgs:
            if img.get('class') == 'gif':
                continue
            img_url = img.xpath(".//@data-original")[0]
            suffix = os.path.splitext(img_url)[1]
            alt = img.xpath(".//@alt")[0]
            alt = re.sub(r'[，。？?,/\\.]','',alt)
            img_name = alt+suffix
            self.img_queue.put((img_url,img_name))
#消费者  图片队列中取出 然后进行下载
class Consumer(threading.Thread):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
    }

    def __init__(self, img_queue,page_queue,*args, **kwargs):
        super(Consumer, self).__init__(*args, **kwargs)
        self.img_queue = img_queue
        self.page_queue = page_queue

    def run(self):
        #从图片队列中取出 图片的url 然后进行下载
        while True:
            if self.img_queue.empty():
                if self.page_queue.empty():
                    return
            img = self.img_queue.get()
            url,filename = img
            request.urlretrieve(url,'images/'+filename)
            print(filename+" 下载完成")



def main():
    #页面的队列
    page_queue = Queue(88)
    #存放图片
    img_queue = Queue(998)

    for x in range(1,89):
        url = "http://www.doutula.com/photo/list/?page=%d" % x
        page_queue.put(url)

    for x in range(5):
        t = Producer(page_queue,img_queue)
        t.start()

    for x in range(5):
        t = Consumer(img_queue,page_queue)
        t.start()

if __name__ == "__main__":
    main()