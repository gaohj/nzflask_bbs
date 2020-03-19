# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exporters import JsonLinesItemExporter
class SoufangPipeline(object):
    def __init__(self):
        self.newhouuse_fp = open('newhouse.json','wb')
        self.esf_fp = open('esf.json','wb')
        self.newhouse_exporter = JsonLinesItemExporter(self.newhouuse_fp,ensure_ascii=False,encoding='utf-8')
        self.esfhouse_exporter = JsonLinesItemExporter(self.esf_fp,ensure_ascii=False,encoding='utf-8')
    def process_item(self, item, spider):
        self.newhouse_exporter.export_item(item)
        self.esfhouse_exporter.export_item(item)
        return item
    def close_spider(self,spider):
        self.newhouuse_fp.close()
        self.esf_fp.close()

