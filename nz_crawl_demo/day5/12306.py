#手动登录

#跳转到购票页面

#手动输入出发地 目的地 出发日期 然后找到查询按钮 点击   进入车次查询

#找到需要的车次 查看对应的席位是否还有余票  有 和数字  如果没有出现这两项 那么循环查询

#一旦出现了 点击 预订 按钮

#来到 预订界面  找到对应的乘客  点击复选框  自动点击提交订单按钮

#点击确认 按钮  就完成了 抢票

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class QiangPiao(object):
    def __init__(self):
        self.login_url = 'https://kyfw.12306.cn/otn/resources/login.html' #登录页面
        self.profile_url = 'https://kyfw.12306.cn/otn/view/index.html' #个人中心页面
        self.search_url = 'https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc' #查票界面
        self.passenger_url = 'https://kyfw.12306.cn/otn/confirmPassenger/initDc' #订单界面
        self.driver = webdriver.Chrome()

    def wait_input(self):
        self.from_station = input("出发地")
        self.to_station = input("目的地")
        self.depart_time = input("出发时间") # yyyy-MM-dd
        self.passengers = input("乘客姓名:多个乘客英文,隔开:").split(',')
        self.trains = input("车次:多个车次英文,隔开:").split(',')

    def _login(self):
        self.driver.get(self.login_url)
        WebDriverWait(self.driver,100).until(
            EC.url_to_be(self.profile_url)
        )
        print("登录成功")



    def run(self):
        self.wait_input()
        self._login()


if __name__ == "__main__":
    spider = QiangPiao()
    spider.run()






