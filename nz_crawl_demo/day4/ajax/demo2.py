from selenium import webdriver


driver = webdriver.Chrome()
driver.get("https://www.zhihu.com/")

print(driver.page_source)