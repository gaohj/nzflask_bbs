# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os
from urllib import request
class AutohomePipeline(object):
    def __init__(self):
        self.path = os.path.join(os.path.dirname(os.path.dirname(__file__)),'images')
        if not os.path.exists(self.path):
            os.mkdir(self.path)

    def process_item(self, item, spider):
        category = item['category']
        urls = item['urls']

        category_path = os.path.join(self.path,category)
        if not os.path.exists(category_path):
            os.mkdir(category_path)
        for url in urls:
            image_name = url.split("_")[-1]
            request.urlretrieve(url,os.path.join(category_path,image_name))
        return item
from scrapy.pipelines.images import ImagesPipeline
from autohome import settings
class Bmw8Pipeline(ImagesPipeline):
    #发送下载请求之前调用这个方法 获取图片url地址和 分类
    #本身就是发送下载请求的
    def get_media_requests(self, item, info):
        request_objs = super(Bmw8Pipeline, self).get_media_requests(item, info)
        for request_obj in request_objs:
            request_obj.item =item
        return request_objs


    def file_path(self, request, response=None, info=None):
        path = super(Bmw8Pipeline, self).file_path(request,response,info)
        # print(path)
        category = request.item.get('category')
        print(category)
        images_store =settings.IMAGES_STORE
        category_path = os.path.join(images_store,category)
        if not os.path.exists(category_path):
            os.mkdir(category_path)
        image_name = path.replace("full/","")
        image_path = os.path.join(category_path,image_name)
        return image_path