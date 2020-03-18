# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from jianshu.items import JianshuItem

class JsSpider(CrawlSpider):
    name = 'js'
    allowed_domains = ['jianshu.com']
    start_urls = ['http://jianshu.com/']

    rules = (
        Rule(LinkExtractor(allow=r'.*/[cp]{1}/[0-9a-z]{12}.*'), callback='parse_detail', follow=True),
    )

    def parse_detail(self, response):
        title = response.xpath("//h1[@class='_1RuRku']/text()").get()
        # author = response.xpath("//div['_3U4Smb']/span[@class='FxYr8x']/a/text()").get()
        # print(author)
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        url = response.url
        article_id = url.split("/")[-1]
        content = response.xpath('//*[@id="__next"]/div[1]/div/div/section[1]/article').getall()
        contents = "".join(content).strip()
        item = JianshuItem(title=title,article_id=article_id,content=content)
        yield item
