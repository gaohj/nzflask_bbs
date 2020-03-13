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
    def _order_ticket(self):
        #查余票界面
        self.driver.get(self.search_url)
        #等待出发地是否输入正确
        WebDriverWait(self.driver,100).until(
            EC.text_to_be_present_in_element_value((By.ID,'fromStationText'),self.from_station)
        )
        # 等待目的地是否输入正确
        WebDriverWait(self.driver, 100).until(
            EC.text_to_be_present_in_element_value((By.ID, 'toStationText'), self.to_station)
        )
        # 等待日期是否输入正确
        WebDriverWait(self.driver, 100).until(
            EC.text_to_be_present_in_element_value((By.ID, 'train_date'),self.depart_time)
        )

        #查询按钮是否可用
        WebDriverWait(self.driver, 100).until(
            EC.element_to_be_clickable((By.ID, 'query_ticket'))
        )

        #如果能够被点击  那么 找到它

        searchBtn = self.driver.find_element_by_id('query_ticket')
        searchBtn.click()

        #等待车次是否展示出来了
        WebDriverWait(self.driver,100).until(
            EC.presence_of_element_located((By.XPATH, './/tbody[@id="queryLeftTable"]/tr'))
        )

        #查找包含车次信息的 tr

        tr_list = self.driver.find_elements_by_xpath("//*[@id='queryLeftTable']/tr[not(@datatan)]")
        print(tr_list)
        for tr in tr_list:
            #获取车次的信息
            train_num = tr.find_element_by_class_name("number").text
            if train_num in self.trains:
                #二等座
                left_ticket = tr.find_element_by_xpath(".//td[4]").text
                print(left_ticket)
                if left_ticket == '有' or left_ticket.isdigit:
                    orderBtn = tr.find_element_by_class_name('btn72')
                    orderBtn.click()
                    #等待是否来到确认订单的页面
                    WebDriverWait(self.driver, 100).until(
                        EC.url_to_be(self.passenger_url)
                    )

                    #所有的乘客是否被加载过来了
                    WebDriverWait(self.driver, 100).until(
                        EC.presence_of_element_located((By.XPATH,".//ul[@id='normal_passenger_id']/li"))
                    )

                    passengers_labels = self.driver.find_elements_by_xpath(".//ul[@id='normal_passenger_id']/li/label")
                    for passengers_label in passengers_labels:
                        name = passengers_label.text
                        if name in self.passengers:
                            passengers_label.click()

                    #获取提交订单的按钮
                    submitBtn = self.driver.find_element_by_id('submitOrder_id')
                    submitBtn.click()

                    #等待出来对话框
                    WebDriverWait(self.driver, 100).until(
                        EC.presence_of_element_located((By.CLASS_NAME,'dhtmlx_wins_body_outer'))
                    )

                    #等待按钮是否也出现了
                    WebDriverWait(self.driver, 100).until(
                        EC.presence_of_element_located((By.ID, 'qr_submit_id'))
                    )
                    #确认按钮
                    confirmBtn = self.driver.find_element_by_id('qr_submit_id')
                    confirmBtn.click()



    def run(self):
        self.wait_input()
        self._login()
        self._order_ticket()


if __name__ == "__main__":
    spider = QiangPiao()
    spider.run()






