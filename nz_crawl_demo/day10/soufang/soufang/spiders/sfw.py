# -*- coding: utf-8 -*-
import scrapy
import re
from soufang.items import NewHouseItem,EsfHouseItem
from scrapy_redis.spiders import RedisSpider

class SfwSpider(RedisSpider):
    name = 'sfw'
    allowed_domains = ['fang.com']
    # start_urls = ['https://www.fang.com/SoufunFamily.htm']
    # 这个方法是拿出新房和二手房的 url
    redis_key = "fang:start_urls"

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
                # print(province)
                yield scrapy.Request(url=newhouse_url,callback=self.parse_newhouse,meta={"info":(province,city)})
                yield scrapy.Request(url=erf_url,callback=self.parse_esf,meta={"info":(province,city,erf_url)})
                # break
            # break
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
            address = li.xpath(".//div[@class='address']/a/@title").get()
            district_text = "".join(li.xpath(".//div[@class='address']/a//text()").getall())
            district_text = re.sub(r'\s',"",district_text)
            district = re.search(r".*\[(.+)\].*",district_text).group(1)
            price = "".join( li.xpath(".//div[@class='nhouse_price']//text()").getall())
            price = re.sub(r"\s|广告","",price)
            sale =  li.xpath(".//div[@class='fangyuan']/span/text()").get()
            origin_url = li.xpath(".//div[@class='nlcd_name']/a/@href").get()
            origin_url = response.urljoin(origin_url)
            item = NewHouseItem(province=province,city=city,name=name,rooms=rooms,area=area,address=address,district=district,sale=sale,price=price,origin_url=origin_url)
            yield item

        next_url = response.xpath("//div[@class='page']//a[@class='next']/@href").get()
        if next_url:
            yield scrapy.Request(url=response.urljoin(next_url),callback=self.parse_newhouse,meta={"info":(province,city)})
    #二手房的内容
    def parse_esf(self,response):
        province, city,erf_url = response.meta.get('info')
        print(erf_url)

        dls = response.xpath("//div[contains(@class,'shop_list')]/dl")
        for dl in dls:
            item = EsfHouseItem(province=province,city=city)
            item['name'] = dl.xpath(".//h4[@class='clearfix']/a/span/text()").get()
            infos = dl.xpath(".//p[@class='tel_shop']/text()").getall()
            infos = list(map(lambda x:re.sub(r'\s',"",x),infos))
            for info in infos:
                if "厅" in info:
                    item['rooms'] = info
                elif "㎡" in info:
                    item['area'] = info
                elif "层" in info:
                    item['floor'] = info
                elif "向" in info:
                    item['toward'] = info
                else:
                    item['year'] = info.replace("年建","")
            item['address'] = dl.xpath(".//p[@class='add_shop']/span/text()").get()
            item['price'] = "".join(dl.xpath(".//dd[@class='price_right']/span[1]//text()").getall())
            item['unit'] = "".join(dl.xpath(".//dd[@class='price_right']/span[2]//text()").getall())
            item['origin_url'] = response.urljoin(dl.xpath(".//h4[@class='clearfix']/a/@href").get())
            yield item
        for x in range(101):
            next_url = erf_url+'house/i3%d/' % x
            yield scrapy.Request(url=response.urljoin(next_url), callback=self.parse_esf,
                                 meta={"info": (province, city)})
