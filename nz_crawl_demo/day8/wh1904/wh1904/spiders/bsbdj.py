# -*- coding: utf-8 -*-
import scrapy
#项目名.items
from wh1904.items import Wh1904Item

class BsbdjSpider(scrapy.Spider):
    name = 'bsbdj'
    allowed_domains = ['budejie.com']
    start_urls = ['http://www.budejie.com/text/1']
    base_domain = 'https://www.budejie.com/text/'
    def parse(self, response):
        outerbox = response.xpath("//div[@class='j-r-list-c-desc']")
        for box in outerbox:
            joke = box.xpath('.//text()').getall()
            joke = "".join(joke).strip()
            link = box.xpath(".//a/@href").get()
            link  = 'http://www.budejie.com'+link
            item = Wh1904Item(joke=joke,link=link)
            yield item
        for x in range(1,50):
            next_url = str(self.base_domain) + str(x)
            yield scrapy.Request(next_url,callback=self.parse)
            x += 1


