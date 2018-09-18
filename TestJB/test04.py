from time import sleep
import time
import sys
from selenium import webdriver
import unittest
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class test01(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://git.lilianinfo.com:4044")
        self.driver.find_element_by_class_name("username").send_keys("0")
        self.driver.find_element_by_class_name("password").send_keys("88998877")
        # 点击登陆按钮
        self.driver.find_element_by_xpath(".//*[@id='react-content']/div/div[2]/form/a").click()
        # 浏览器最大化
        self.driver.maximize_window()
        sleep(1)

    def tearDown(self):
        sleep(2)
        self.driver.find_element_by_css_selector(".navbarlsta.personmenu>span").click()
        sleep(1)
        self.driver.find_element_by_xpath(".//*[@id='personal']/div/div[2]/div[2]/button").click()
        sleep(2)
        self.driver.quit()

    def test001(self):
        driver = self.driver
        driver.implicitly_wait(30)

        # 点击导航栏
        driver.find_element_by_css_selector(".icon.iconfont.icon-Expand").click()

        # 点击病例预警主菜单
        driver.find_element_by_xpath(".//*[@id='lteNav']/li[2]/p/p/span").click()

        # 点击病例预警子菜单
        driver.find_element_by_xpath(".//*[@id='ltewrap']/div[2]/div/ul/li[1]/a").click()

        sleep(2)
        driver.find_element_by_xpath(".//*[@id='maincontent']/div/div[2]/div/div[2]/div[1]/div/div[2]/div/div/div[1]/div/div[1]/div/div/div/div/div/div/div[2]/table/tbody/tr[3]/td[3]/div").click()
        sleep(1)
        driver.find_element_by_xpath(".//*[@id='maincontent']/div/div[2]/div/div[2]/div[1]/div/div[2]/div/div/div[3]/div[1]/div/div/div/div/div/div/div[2]/table/tbody/tr[1]/td[3]/div/div/div/div/div").click()

        # try:
        #     sleep(2)
        #     # text1 = driver.find_element_by_css_selector(".ant-select-dropdown-menu-item-active.ant-select-dropdown-menu-item-selected.ant-select-dropdown-menu-item").text
        #     text2 = driver.find_element_by_class_name("ant-select-dropdown-menu-item-active").text
        #     # text3 = driver.find_element_by_css_selector("").text
        #     # text4 = driver.find_element_by_css_selector("").text
        #     # text5 = driver.find_element_by_xpath("/html/body/div[4]/div/div/div/ul/li[5]").text
        #     # text6 = driver.find_element_by_xpath("/html/body/div[4]/div/div/div/ul/li[6]").text
        #
        #     # print("提示的信息为：", text1)
        #     print("提示的信息为：", text2)
        #     # print("提示的信息为：", text3)
        #     # print("提示的信息为：", text4)
        #     # print("提示的信息为：", text5)
        #     # print("提示的信息为：", text6)
        #     # 断言
        #
        #     # self.assertEqual("疑似", text1)
        #     self.assertEqual("院内", text2)
        #     # self.assertEqual("院外", text3)
        #     # self.assertEqual("排除", text4)
        #     # self.assertEqual("待查", text5)
        #     # self.assertEqual("转归", text6)
        # except AssertionError:
        #     print("获取的sys.exc_info()信息为:", sys.exc_info()[1])
        #     nowtime = time.strftime("%Y_%m_%d %H_%M_%S")
        #
        #     print("时间格式为：", nowtime)
        #     driver.get_screenshot_as_file("../Image/%s-%s.jpg" % (nowtime, "test_107在院病例预警疑似初始显示"))
        #     # 抛异常
        #     raise
        try:

            text1 = driver.find_element_by_xpath("html/body/div[2]/div/div/div/ul/li[1]").text
            text2 = driver.find_element_by_xpath("html/body/div[2]/div/div/div/ul/li[2]").text
            # text3 = driver.find_element_by_xpath("html/body/div[2]/div/div/div/ul/li[3]").text
            # text4 = driver.find_element_by_xpath("html/body/div[2]/div/div/div/ul/li[4]").text
            # text5 = driver.find_element_by_xpath("html/body/div[2]/div/div/div/ul/li[5]").text
            # text6 = driver.find_element_by_xpath("html/body/div[2]/div/div/div/ul/li[6]").text
            print("提示的信息为：", text1)
            print("提示的信息为：", text2)
            # print("提示的信息为：", text3)
            # print("提示的信息为：", text4)
            # print("提示的信息为：", text5)
            # print("提示的信息为：", text6)
            assert text1 == "疑似"
            assert text1 == "院内"
            # assert text1 == "院外"
            # assert text1 == "排除"
            # assert text1 == "待查"
            # assert text1 == "转归"
            print(text1)
            print(text2)
            # print(text3)
            # print(text4)
            # print(text5)
            # print(text6)
        except Exception as e:
            # print("获取的sys.exc_info()信息为:", sys.exc_info()[1])
            print("测试失败", format(e))
            nowtime = time.strftime("%Y_%m_%d %H_%M_%S")
            print("时间格式为：", nowtime)
            driver.get_screenshot_as_file("../Image/%s-%s.jpg" % (nowtime, "test_107在院病例预警疑似初始显示"))



if __name__ == '__main__':
    unittest.main()