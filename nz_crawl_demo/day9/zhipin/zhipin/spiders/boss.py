# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BossSpider(CrawlSpider):
    name = 'boss'
    allowed_domains = ['zhipin.com']
    start_urls = ['https://www.zhipin.com/c100010000/?query=python&page=1']

    rules = (
        Rule(LinkExtractor(allow=r'.+query=python&page=\d'),follow=True),
        Rule(LinkExtractor(allow=r'.+job_detail/[0-9a-zA-Z~_]+\.html'), callback='parse_job', follow=False),
    )

    def parse_job(self, response):
        print(88888)
        name = response.xpath("//h1/text()").get()
        print(name)
        item = {}
        return item
