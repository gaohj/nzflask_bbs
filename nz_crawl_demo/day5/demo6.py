from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
suBtn = driver.find_element_by_id('su')
print(suBtn.get_attribute('value'))
driver.save_screenshot('baidu.png')



