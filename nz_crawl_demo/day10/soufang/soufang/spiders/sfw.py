# -*- coding: utf-8 -*-
import scrapy
import re

class SfwSpider(scrapy.Spider):
    name = 'sfw'
    allowed_domains = ['fang.com']
    start_urls = ['https://www.fang.com/SoufunFamily.htm']
    # 这个方法是拿出新房和二手房的 url
    def parse(self, response):
        trs = response.xpath("//div[@class='outCont']//tr")
        for tr in trs:
            tds = tr.xpath(".//td[not(@class)]")
            province_td = tds[0]
            provice_text = province_td.xpath(".//text()").get()
            provice_text = re.sub(r'\s',"",provice_text)
            if provice_text:
                province = provice_text

                if province == '其它':
                    continue


    # 新房的内容
    def parse_newhouse(self,response):
        pass

    #二手房的内容
    def parse_esf(self,response):
        pass
