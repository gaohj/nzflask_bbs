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
            city_td = tds[1]
            city_links = city_td.xpath(".//a")
            for city_link in city_links:
                city = city_link.xpath(".//text()").get()
                city_url = city_link.xpath(".//@href").get()
                # print("省份:%s" % province)
                # print("城市:%s" % city)
                # print("链接:%s" % city_url)
                #构建新房url
                url_module = city_url.split(".")
                scheme = url_module[0]
                domain = url_module[1]
                com = url_module[2]
                # print(scheme)
                # print(domain)
                if "bj" in scheme.split("//")[1]:
                    newhouse_url = "https://newhouse.fang.com/house/s/"
                    erf_url = 'https://esf.fang.com/'
                else:
                    newhouse_url = scheme+".newhouse."+domain+'.'+com+'house/s/'
                    erf_url = scheme+'.esf.'+domain+'.'+com

                # print("新房%s" % newhouse_url)
                # print("二手房%s" % erf_url)
                yield scrapy.Request(url=newhouse_url,callback=self.parse_newhouse,meta={"info":(province,city)})
                # yield scrapy.Request(url=erf_url,callback=self.parse_esf,meta={"info":(province,city)})
                break
            break
    # 新房的内容
    def parse_newhouse(self,response):
        province,city = response.meta.get('info')
        lis = response.xpath("//div[contains(@class,'nl_con')]/ul/li")
        for li in lis:
            try:
                name = li.xpath(".//div[@class='nlcd_name']/a/text()").get().strip()
            except:
                pass
            house_type_list = li.xpath(".//div[contains(@class,'house_type')]/a/text()").getall()
            house_type_list = list(map(lambda x:re.sub(r'\s',"",x),house_type_list))
            rooms = list(filter(lambda x:x.endswith("居"),house_type_list))
            area = "".join(li.xpath(".//div[contains(@class,'house_type')]/text()").getall())
            area = re.sub(r'\s|－|/|',"",area)
            print(area)

    #二手房的内容
    def parse_esf(self,response):
        pass
