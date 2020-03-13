from selenium import webdriver

import time

driver = webdriver.Chrome()
driver.get("https://www.douban.com/")

driver.execute_script("window.open('https://www.baidu.com/')")
driver.execute_script("window.open('https://www.zhihu.com/')")

print(driver.window_handles) #窗口的句柄
driver.switch_to_window(driver.window_handles[1])

