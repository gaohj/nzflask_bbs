# -*- coding: utf-8 -*-
import scrapy


class XiaoqiangSpider(scrapy.Spider):
    name = 'xiaoqiang'
    allowed_domains = ['qiangqiang.com']
    start_urls = ['http://qiangqiang.com/']

    def parse(self, response):
        pass
