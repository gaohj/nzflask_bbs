from lxml import etree
parser = etree.HTMLParser(encoding='utf-8')
html = etree.parse('tencent.html',parser=parser)

# 获取所有的tr标签
# trs = html.xpath("//tr")
# for tr in trs:
#     #toString返回的是bytes类型  decode 将bytes 转为 string
#     res = etree.tostring(tr,encoding='utf-8').decode('utf-8')
#     # print(res)

#获取第二个tr标签
tr = html.xpath("//tr[2]")[0]
print(etree.tostring(tr,encoding='utf-8').decode('utf-8'))

#获取所有class 为 event的 tr 标签

trs = html.xpath("//tr[@class='even']")
for tr in trs:
    print(etree.tostring(tr,encoding='utf-8').decode('utf-8'))

#获取所有a标签的 href 属性
aList = html.xpath("//a/@href")
for a in aList:
    print("http://hr.tencent.com/" + a)
#获取所有的职位信息
trs = html.xpath('//tr[position()>1]')
positions = [] #用来存放所有的结果
for tr in trs:
    href = tr.xpath(".//a/@href")[0]
    fullurl = "http://hr.tencent.com/" + href
    title = tr.xpath("./td[1]//text()")[0]
    category =tr.xpath("./td[2]//text()")[0]
    nums =tr.xpath("./td[3]//text()")[0]
    address =tr.xpath("./td[4]//text()")[0]
    pubtime =tr.xpath("./td[5]//text()")[0]
    position = {
        'url':fullurl,
        'title':title,
        'category':category,
        'nums':nums,
        'address':address,
        'pubtime':pubtime,
    }
    positions.append(position)
print(positions)