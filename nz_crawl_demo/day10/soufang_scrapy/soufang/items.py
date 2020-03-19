# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NewHouseItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #省份
    province = scrapy.Field()
    # 城市
    city = scrapy.Field()
    # 小区名字
    name = scrapy.Field()
    #价格
    price = scrapy.Field()
    #几居室
    rooms = scrapy.Field()
    #面积
    area = scrapy.Field()
    #地址
    address = scrapy.Field()
    #区域
    district = scrapy.Field()
    #是否在售
    sale = scrapy.Field()
    #小区详情
    origin_url = scrapy.Field()

class EsfHouseItem(scrapy.Item):
    #省份
    province = scrapy.Field()
    # 城市
    city = scrapy.Field()
    # 小区名字
    name = scrapy.Field()
    #价格
    price = scrapy.Field()
    #几居室
    rooms = scrapy.Field()
    # 几层
    floor = scrapy.Field()
    # 朝向
    toward = scrapy.Field()
    #面积
    area = scrapy.Field()
    #地址
    address = scrapy.Field()
    #区域
    unit = scrapy.Field()
    #小区详情
    origin_url = scrapy.Field()
    #年份
    year = scrapy.Field()