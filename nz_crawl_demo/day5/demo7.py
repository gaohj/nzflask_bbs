from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()

driver.get("https://www.baidu.com/")
# driver.implicitly_wait(5) #获取不可用的元素  如果能返回就不等
#
# #上面的代码 就是 等五秒以后 给你返回错误
# print(driver.page_source)

element = WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.ID,'su'))
)

print(element)