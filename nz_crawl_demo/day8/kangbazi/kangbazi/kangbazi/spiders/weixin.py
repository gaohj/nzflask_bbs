# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from kangbazi.items import KangbaziItem

class WeixinSpider(CrawlSpider):
    name = 'weixin'
    allowed_domains = ['wxapp-union.com']
    start_urls = ['http://www.wxapp-union.com/portal.php?mod=list&catid=2&page=1']

    rules = (
        Rule(LinkExtractor(allow=r'.+mod=list&catid=2&page=\d'),follow=True), #如果继续跟进那么不需要回调函数
        Rule(LinkExtractor(allow=r'.+article-.+\.html'), callback='parse_detail', follow=False),#不跟进写回调函数
    )

    # def parse(self): #这个方法命名 不能叫parse 因为 底层的方法名就叫parse
    #如果这里命名 parse  那么底层的parse方法就失效了
    def parse_detail(self, response):
        item = {}
        title = response.xpath('//h1[@class="ph"]/text()').get()
        p = response.xpath('//p[@class="authors"]')
        author= p.xpath('.//a/text()').get()
        pub_time = p.xpath('.//span/text()').get()
        article_content= response.xpath('//*[@id="article_content"]').getall()
        content = "".join(article_content).strip()
        item = KangbaziItem(title=title,content=content,pub_time=pub_time,author=author)
        yield item
