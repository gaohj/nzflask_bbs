# 使用代理
from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_argument("--proxy-server=http://175.10.24.127:3128")
options.add_argument("--headless") #不打开浏览器
options.add_argument("--disable-gpu") #禁用gpu


driver = webdriver.Chrome(chrome_options=options)
driver.get("http://httpbin.org/ip")
print(driver.page_source)