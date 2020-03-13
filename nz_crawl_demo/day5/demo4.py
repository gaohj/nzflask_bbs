from selenium import webdriver

import time

driver = webdriver.Chrome()
driver.get("https://www.douban.com/")

# print(driver.get_cookies())
for cookie in driver.get_cookies():
    print(cookie)

print(driver.get_cookie('bid'))

print(driver.delete_cookie('bid'))
print("*"*30)
for cookie in driver.get_cookies():
    print(cookie)

print("*"*30)

driver.delete_all_cookies()
print("6"*30)
for cookie in driver.get_cookies():
    print(cookie)
