# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals


class ZhipinSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class ZhipinDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)

import random
class BossUserAgentDownloadMiddleware(object):
    USER_AGENTS =[
        'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11',
        'Mozilla/5.0 (X11; Linux i686; rv:64.0) Gecko/20100101 Firefox/64.0',

    ]

    def process_request(self,request,spider):
        user_agent = random.choice(self.USER_AGENTS)
        request.headers['User-Agent'] = user_agent

import base64
# class IpproxyDownloadMiddleware(object):
#
#     def process_request(self,request,spider):
#         proxy = "49.7.96.227:16817"
#         user_password = "gaohj5:ddk5fr4z"
#         b64_user_password = base64.b64encode(user_password.encode("utf-8"))
#         request.headers["Proxy-Authorization"] = "Basic " + b64_user_password.decode("utf-8")
#         return None
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from scrapy.http.response.html import HtmlResponse
class SeleniumMiddleware(object):

    def __init__(self):
        self.options = Options()
        self.options.add_argument("--headless")
        # self.options.add_argument("--proxy-server:http://")
        self.driver = webdriver.Chrome(chrome_options=self.options)


    def process_request(self,request,spider):
        self.driver.get(request.url)
        time.sleep(1)
        source = self.driver.page_source
        print(source)
        #截获请求让谷歌浏览器去发送，再返回
        response = HtmlResponse(url=self.driver.current_url,body=source,request=request,encoding='utf-8')

        return response

import requests
import json
from .models import ProxyModel
class IpproxyDownloadMiddleware(object):
    PROXY_URL = 'http://http.tiqu.alicdns.com/getip3?num=1&type=2&pro=0&city=0&yys=0&port=1&time=1&ts=1&ys=0&cs=0&lb=1&sb=0&pb=4&mr=2&regions=&gm=4'
    def __init__(self):
        super(IpproxyDownloadMiddleware, self).__init__()
        self.current_proxy = None
    def process_request(self,request,spider):
        if 'proxy' not in request.meta or self.current_proxy.is_expiring:
            self.update_proxy()
        request.meta['proxy'] = self.current_proxy.proxy
        print(request.meta['proxy'])

    # def process_reponse(self,request,response,spider):
    #     return None

    #用来更新代理IP的
    def update_proxy(self):
        response = requests.get(self.PROXY_URL)
        text = response.text
        print("重新获取了一个代理",text)
        #芝麻代理不让频繁的发送请求 否则data没有值
        result = json.loads(text)
        if len(result['data'])>0:
            data = result['data'][0]
            proxy_model = ProxyModel(data)
            self.current_proxy = proxy_model

