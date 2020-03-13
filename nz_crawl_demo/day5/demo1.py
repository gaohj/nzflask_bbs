from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("http://www.zhihu.com")

time.sleep(2)
# driver.quit()
driver.close()
