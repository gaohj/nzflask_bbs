from selenium import webdriver
from lxml import etree
import time
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
# driver.get("https://www.zhihu.com/signin?next=%2F")
# driver.get("https://www.baidu.com/")
driver.get("https://v3.bootcss.com/examples/signin/")
html = driver.page_source

# html = etree.HTML(html)
# elements = html.xpath("//input[@name='username']/@placeholder")[0]
# print(elements)

# inputTag = driver.find_element(By.XPATH,"//input[@name='username']")
# inputTag = driver.find_element(By.NAME,"username")
# inputTag = driver.find_element(By.CSS_SELECTOR,".SignFlow-accountInput > .Input")
# inputTag = driver.find_element(By.ID,".SignFlow-accountInput > .Input")
# inputTag = driver.find_element(By.CLASS_NAME,"Input")
# inputTag.send_keys('13888888888')
# time.sleep(3)
# inputTag.clear()
# inputTag = driver.find_element_by_id('kw')
# inputTag.send_keys('python')
# time.sleep(2)
# # inputTag.clear()
# submitTag = driver.find_element_by_id('su')
# submitTag.click()

reBtn = driver.find_element_by_css_selector('label > input ')
reBtn.click()