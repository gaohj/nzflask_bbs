from selenium import webdriver #导入驱动器

dirver_path = r"C:\chromedriver_win32\chromedriver.exe" #指明驱动器位置
driver = webdriver.Chrome(executable_path=dirver_path)
driver.get("https://www.baidu.com")  #请求url
print(driver.page_source) #获取网页源代码