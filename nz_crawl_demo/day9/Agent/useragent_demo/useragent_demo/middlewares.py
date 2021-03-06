# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals


class UseragentDemoSpiderMiddleware(object):
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

import random
class UserAgentDownloadMiddleware(object):
    USER_AGENTS =[
        'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11',
        'Mozilla/5.0 (X11; Linux i686; rv:64.0) Gecko/20100101 Firefox/64.0',

    ]

    def process_request(self,request,spider):
        user_agent = random.choice(self.USER_AGENTS)
        request.headers['User-Agent'] = user_agent

    # def process_response(self,request,spider):
    #     pass

# class IpproxyDownloadMiddleware(object):
#     PROXIES =[
#         "http://118.112.195.179:9999",
#         "http://39.137.69.7:8080",
#         "http://221.180.170.104:8080",
#         "http://39.137.95.74:80",
#     ]
#
#     def process_request(self,request,spider):
#         proxy = random.choice(self.PROXIES)
#         request.meta['proxy'] = proxy
import base64
class IpproxyDownloadMiddleware(object):

    def process_request(self,request,spider):
        proxy = "49.7.96.227:16817"
        user_password = "gaohj5:ddk5fr4z"
        b64_user_password = base64.b64encode(user_password.encode("utf-8"))
        request.headers["Proxy-Authorization"] = "Basic " + b64_user_password.decode("utf-8")
        return None

