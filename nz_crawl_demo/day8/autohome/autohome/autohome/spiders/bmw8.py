# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from autohome.items import AutohomeItem

class Bmw8Spider(CrawlSpider):
    name = 'bmw8'
    allowed_domains = ['car.autohome.com.cn']
    start_urls = ['https://car.autohome.com.cn/pic/series/3464.html']

    rules = (
        Rule(LinkExtractor(allow=r'https://car.autohome.com.cn/pic/series/3464.+'), callback='parse_page', follow=True),
    )

    def parse_page(self, response):
        uiboxes = response.xpath("//div[@class='uibox']")[1:]
        for uibox in uiboxes:
            category = uibox.xpath(".//div[@class='uibox-title']/a/text()").get()
            urls = uibox.xpath(".//ul/li/a/img/@src").getall()
            # for url in urls:
            #     url = response.urljoin(url)
            #     print(url)
            urls = list(map(lambda url:response.urljoin(url),urls))
            item = AutohomeItem(category=category,urls=urls)
            yield item
