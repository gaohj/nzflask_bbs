from selenium import webdriver
from lxml import etree
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
inputTag = driver.find_element_by_id('kw')
subTag = driver.find_element_by_id('su')

actions = ActionChains(driver)
actions.move_to_element(inputTag)
actions.send_keys_to_element(inputTag,'python')
actions.move_to_element(subTag)
actions.click(subTag)
actions.perform()
