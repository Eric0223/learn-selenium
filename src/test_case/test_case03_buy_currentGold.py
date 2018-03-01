# -*- coding:utf-8 -*-
'''
Created on 2017/12/18/018 23:39
@author: luox
Description: 测试购买流动金
'''
import unittest
from selenium import webdriver
from src.pages.buyCurrentGold_page import BuyCurrentGold
from src.pages.login_page import LoginPage
from time import sleep
from config.globalparameter import profile


class TestBuyCurrentGold(unittest.TestCase):
    u'''买金测试'''
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox(profile)
        login_page = LoginPage(cls.driver)
        login_page.open_login_page()
        login_page.choose_tab_password()
        login_page.input_username("18503035162")
        login_page.input_password("a123456")
        login_page.click_btn_login_pwd()
        sleep(3)

    def test_01(self):
        u'''购买流动金，按克数购买'''
        self.buyGold_page = BuyCurrentGold(self.driver)
        self.buyGold_page.open_currentGold_page()
        sleep(3)
        self.buyGold_page.click_btn_currentGold()
        sleep(1)
        self.buyGold_page.input_grams("1")
        self.buyGold_page.click_btn_buy()
        self.buyGold_page.click_btn_next()
        sleep(3)
        self.buyGold_page.input_trading_password("111111")
        self.buyGold_page.click_btn_pay_immediately()
        sleep(3)

    def test_02(self):
        u'''购买流动金，按金额购买'''
        self.buyGold_page = BuyCurrentGold(self.driver)
        self.buyGold_page.open_currentGold_page()
        sleep(3)
        self.buyGold_page.click_btn_currentGold()
        sleep(1)
        self.buyGold_page.buy_by_money()
        self.buyGold_page.input_money("100")
        self.buyGold_page.click_btn_buy()
        self.buyGold_page.click_btn_next()
        sleep(3)
        self.buyGold_page.input_trading_password("111111")
        self.buyGold_page.click_btn_pay_immediately()
        sleep(3)


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()