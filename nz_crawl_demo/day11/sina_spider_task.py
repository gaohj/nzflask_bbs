'''
@Author  : hallen
@Contact : QQ:2713058923
@Time   :   2019-09-23
@Desc   :

'''
import json

import requests
import pymysql
from apps import app

@app.task()
def get_spider():

    for i in range(5):
        url = 'https://feed.sina.com.cn/api/roll/get?pageid=121&lid=1356&num=20&versionNumber=1.2.4&page={}&encode=utf-8&callback=feedCardJsonpCallback&_=1569240540973'.format(i+1)
        print(url)
        headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',

        }
        res = requests.get(url,headers=headers)
        text = res.content.decode('utf-8')
        # print(text)
        # print(type(text))
        text = text.split('try{feedCardJsonpCallback(')[1]
        # print(text)
        text = text.split(');}catch(e){};')[0]
        # print(text)
        json_data = json.loads(text)
        # print(json_data)
        # print(type(json_data))
        datas = json_data['result']['data']
        conn = pymysql.connect(host='localhost',port=3306,user='root',password='root',database='news',charset='utf8')
        cursor = conn.cursor()
        sql = """insert into new(title,url,ctime) value(%s,%s,%s)"""
        select_sql = """select title,url,ctime from new WHERE title=%s AND url=%s AND ctime=%s"""
        for data in datas:
            # print(data)
            title = data['title']
            url = data['url']
            ctime = data['ctime']
            result = cursor.execute(select_sql,(title,url,ctime))
            # title，url,ctime是不是在数据库中，不在才执行insert语句
            if result == 1:
                continue
            else:
                cursor.execute(sql,(title,url,ctime))
                conn.commit()
        conn.close()


if __name__ == '__main__':
    get_spider()