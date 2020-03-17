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
  #https://car2.autoimg.cn/cardfs/product/g30/M08/72/ED/240x180_0_q95_c42_autohomecar__ChsEf10CSUOAVR9mAAl0KNuQm2o153.jpg
  #https://car2.autoimg.cn/cardfs/product/g30/M08/72/ED/1024x0_1_q95_autohomecar__ChsEf10CSUOAVR9mAAl0KNuQm2o153.jpg
    def parse_page(self, response):
         category = response.xpath("//div[@class='uibox']/div/text()").get()
         srcs = response.xpath("//div[contains(@class,'uibox-con')]/ul/li//img/@src").getall()
         srcs = list(map(lambda url:response.urljoin(url.replace("240x180_0_q95_c42","1024x0_1_q95")),srcs))
         print(srcs)
         item = AutohomeItem(category=category, image_urls=srcs)
         yield item

    def test_page(self, response):
        uiboxes = response.xpath("//div[@class='uibox']")[1:]
        for uibox in uiboxes:
            category = uibox.xpath(".//div[@class='uibox-title']/a/text()").get()
            urls = uibox.xpath(".//ul/li/a/img/@src").getall()
            # for url in urls:
            #     url = response.urljoin(url)
            #     print(url)
            urls = list(map(lambda url:response.urljoin(url),urls))
            item = AutohomeItem(category=category,image_urls=urls)
            yield item
