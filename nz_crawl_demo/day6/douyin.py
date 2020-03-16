#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import requests
from lxml import etree

start_url = ' https://www.iesdouyin.com/share/user/88445518961'

def get_real_num(content):
    content = content.replace(' &#', '0').replace('; ', '')
    regex_list = [
        {'name': ['0xe602', '0xe60e', '0xe618'], 'value': '1'},
        {'name': ['0xe603', '0xe60d', '0xe616'], 'value': '0'},
        {'name': ['0xe604', '0xe611', '0xe61a'], 'value': '3'},
        {'name': ['0xe605', '0xe610', '0xe617'], 'value': '2'},
        {'name': ['0xe606', '0xe60c', '0xe619'], 'value': '4'},
        {'name': ['0xe607', '0xe60f', '0xe61b'], 'value': '5'},
        {'name': ['0xe608', '0xe612', '0xe61f'], 'value': '6'},
        {'name': ['0xe609', '0xe615', '0xe61e'], 'value': '9'},
        {'name': ['0xe60a', '0xe613', '0xe61c'], 'value': '7'},
        {'name': ['0xe60b', '0xe614', '0xe61d'], 'value': '8'}
    ]

    for i1 in regex_list:
        for font_code in i1['name']:
            content = re.sub(font_code, str(i1['value']), content)

    html = etree.HTML(content)
    douyin_info = {}
    # 获取抖音ID
    # douyin_id = ''.join(html.xpath("//div[@class='personal-card']/div[@class='info1']/p[@class='shortid']/text()"))
    # print(douyin_id)
    # douyin_id = douyin_id.replace('抖音ID：', '').replace(' ', '')
    # print(douyin_id)
    i_id = ''.join(html.xpath("//div[@class='personal-card']/div[@class='info1']/p[@class='shortid']/i/text()"))
    douyin_info['douyin_id'] =  str(i_id)
    # print(str(douyin_id))
    print(douyin_info)
    # 关注
    douyin_info['follow_count'] = ''.join(html.xpath(
        "//div[@class='personal-card']/div[@class='info2']/p[@class='follow-info']//span[@class='focus block']//i/text()"))
    # 粉丝
    fans_value = ''.join(html.xpath(
        "//div[@class='personal-card']/div[@class='info2']/p[@class='follow-info']//span[@class='follower block']//i[@class='icon iconfont follow-num']/text()"))

    unit = html.xpath(
        "//div[@class='personal-card']/div[@class='info2']/p[@class='follow-info']//span[@class='follower block']/span[@class='num']/text()")
    if unit[-1].strip() == 'w':
        douyin_info['fans'] = str(float(fans_value) / 10) + 'w'
        fans_count = douyin_info['fans'][:-1]
        fans_count = float(fans_count)
        fans_count = fans_count * 10000
        douyin_info['fans_count'] = fans_count
    else:
        douyin_info['fans'] = fans_value
        douyin_info['fans_count'] = fans_value
    # 点赞
    like = ''.join(html.xpath(
        "//div[@class='personal-card']/div[@class='info2']/p[@class='follow-info']//span[@class='liked-num block']//i[@class='icon iconfont follow-num']/text()"))
    unit = html.xpath(
        "//div[@class='personal-card']/div[@class='info2']/p[@class='follow-info']//span[@class='liked-num block']/span[@class='num']/text()")
    if unit[-1].strip() == 'w':
        douyin_info['like'] = str(float(like) / 10) + 'w'
        like_count = douyin_info['like'][:-1]
        like_count = float(like_count)
        like_count = like_count * 10000
        douyin_info['like_count'] = like_count
    else:
        douyin_info['like'] = like
        douyin_info['like_count'] = like

    # 作品
    worko_count = ''.join(html.xpath("//div[@class='video-tab']/div/div[1]//i/text()"))
    douyin_info['work_count'] = worko_count
    return douyin_info

def get_html():
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'
    }
    response = requests.get(url=start_url, headers=header, verify=False)
    # print(response.text)
    return response.text

def run():
    content = get_html()
    info = get_real_num(content)
    print(info)

if __name__ == '__main__':
    run()