# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from pymysql import cursors

class JianshuPipeline(object):
    def __init__(self):
        dbparams = {
            'host':'rm-2zeurakrzwvrqp7o0qo.mysql.rds.aliyuncs.com',
            'port':3306,
            'user':'',
            'password':'',
            'database':'jianshu',
            'charset':'utf8'
        }

        self.conn = pymysql.connect(**dbparams)
        self.cursors = self.conn.cursor()
        self._sql = None




    def process_item(self, item, spider):
        self.cursors.execute(self.sql,(item['title'],item['content'],item['article_id']))
        self.conn.commit()
        return item

    @property
    def sql(self):
        if not self._sql:
            self._sql = """
                    insert into article(id,title,content,article_id) values (null,%s,%s,%s)
                    """
            return self._sql
        return self._sql



from twisted.enterprise import adbapi
class JianshuTwistedPipeline(object): #采用 twisted 异步id
    def __init__(self):
        dbparams = {
            'host':'rm-2zeurakrzwvrqp7o0qo.mysql.rds.aliyuncs.com',
            'port':3306,
            'user':'',
            'password':'',
            'database':'jianshu',
            'charset':'utf8',
            'cursorclass':cursors.DictCursor
        }

        self.dbpool = adbapi.ConnectionPool('pymysql',**dbparams)
        self._sql = None

    @property
    def sql(self):
        if not self._sql:
            self._sql = """
                insert into article(title,content,article_id) values (%s,%s,%s)
            """
            return self._sql
        return self._sql

    def process_item(self,item,spider):
        defer = self.dbpool.runInteraction(self.insert_item,item) #异步操作
        # defer.addErrback(self.handle_error,item,spider)
    def insert_item(self,cursor,item):
        # print(item['title'],item['content'])
        cursor.execute(self.sql,(item['title'], item['content'], item['article_id']))

    def handle_error(self,error,item,spider):
        print(error)


