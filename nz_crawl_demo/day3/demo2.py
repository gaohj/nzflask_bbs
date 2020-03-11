from lxml import etree

html = etree.parse('tencent.html') #读取外部文件

result = etree.tostring(html,pretty_print=True)
print(result)