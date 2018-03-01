# -*- coding:utf-8 -*-
'''
Created on 2018/2/4/004 13:23
@author: luox
Description: 测试首页各链接跳转是否正常
'''
import unittest
from src.pages.index_page import IndexPage
from selenium import webdriver
from config.globalparameter import profile


class IndexTest(unittest.TestCase):
    '''首页测试'''
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox(profile)
        cls.index_page = IndexPage(cls.driver)
        cls.index_page.open_index_page()

    def test_01(self):
        '''点击买入黄金'''
        self.index_page.click_buy_gold()
        buy_gold_title = u"中国黄金金有金-产品列表-期限灵活"
        # 获取所有窗口的句柄
        all_handle = self.driver.window_handles
        # 切换到新打开的窗口
        self.driver.switch_to.window(all_handle[1])
        current_title = self.driver.title
        self.assertEqual(buy_gold_title, current_title, msg=u"进入买入黄金页面失败")
        # 测试完后关闭当前窗口
        self.driver.close()
        # 切换回首页窗口
        self.driver.switch_to.window(all_handle[0])

    @unittest.skip(u"暂不执行")
    def test_02(self):
        '''点击首页'''
        self.index_page.click_buy_gold()
        all_handle = self.driver.window_handles
        self.driver.switch_to.window(all_handle[1])
        self.index_page.click_index()
        buy_gold_title = u"中国黄金·金有金-我的黄金管家"
        current_title = self.driver.title
        self.assertEqual(buy_gold_title, current_title, msg=u"进入首页失败")
        self.driver.close()
        self.driver.switch_to.window(all_handle[0])

    def test_03(self):
        '''点击黄金账户'''
        self.index_page.click_gold_account()
        gold_account_title = u"中国黄金金有金-登录-互联网黄金理财首选"
        all_handle = self.driver.window_handles
        self.driver.switch_to.window(all_handle[1])
        current_title = self.driver.title
        self.assertEqual(gold_account_title, current_title, msg=u"进入黄金账户页面失败")
        self.driver.close()
        self.driver.switch_to.window(all_handle[0])

    def test_04(self):
        '''点击关于我们'''
        self.index_page.click_about_us()
        about_us_title = u"中国黄金金有金-关于我们-公司介绍"
        all_handle = self.driver.window_handles
        self.driver.switch_to.window(all_handle[1])
        current_title = self.driver.title
        self.assertEqual(about_us_title, current_title, msg=u"进入关于我们页面失败")
        self.driver.close()
        self.driver.switch_to.window(all_handle[0])

    def test_05(self):
        '''点击登录'''
        self.index_page.click_btn_login()
        login_title = u"中国黄金金有金-登录-互联网黄金理财首选"
        current_title = self.driver.title
        self.assertEqual(login_title, current_title, msg=u"进入登录页面失败")
        self.driver.back()

    def test_06(self):
        '''点击注册'''
        self.index_page.click_btn_register()
        register_title = u"中国黄金金有金-登录-互联网黄金理财首选"
        current_title = self.driver.title
        self.assertEqual(register_title, current_title, msg=u"进入注册页面失败")
        self.driver.back()

    def test_07(self):
        '''点击注册领万元本金'''
        self.index_page.click_btn_register_experence()
        register_experience_title = u"中国黄金金有金-登录-互联网黄金理财首选"
        current_title = self.driver.title
        self.assertEqual(register_experience_title, current_title, msg=u"进入注册页面失败")
        self.driver.back()

    def test_08(self):
        '''点击金价走势'''
        self.index_page.click_goldtrend()
        goldtrend_title = u"中国黄金金有金-产品列表-期限灵活"
        current_title = self.driver.title
        self.assertEqual(goldtrend_title, current_title, msg=u"进入金价走势页面失败")

    @classmethod
    def tearDownClass(cls):
        pass

if __name__ == "__main__":
    unittest.main()



