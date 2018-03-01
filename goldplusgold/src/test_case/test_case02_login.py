# -*- coding:utf-8 -*-
'''
Created on 2018/1/30 13:41
@author: luox
description: 测试快捷登录，密码登录功能
'''

import unittest
from selenium import webdriver
from src.pages.login_page import LoginPage
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from src.common.dbClection import DatabaseOperation
from config.globalparameter import profile


class LoginTest(unittest.TestCase):
    u'''登录测试'''
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.username = "18503035162"
        cls.password = "a123456"
        cls.expect_user_id = "185****5162"
        cls.key = "verify_code"
        cls.sql = "SELECT * FROM verify_code WHERE phone = '%s' ORDER BY create_date DESC" % cls.username

    def test_01(self):
        u'''手机号快捷登录测试'''
        self.login_page = LoginPage(self.driver)
        self.login_page.open_login_page()
        self.login_page.input_phone(self.username)
        self.login_page.get_verify_code()
        sleep(1)
        db = DatabaseOperation()
        verfy_code = db.get_data(self.key, self.sql)
        self.login_page.input_verify_code('%s' % verfy_code)
        self.login_page.click_btn_login()
        # 等待时间后续优化
        sleep(3)
        user_id = self.login_page.show_user_id()
        # 判断登录是否成功
        self.assertEqual(user_id, self.expect_user_id, msg='登录失败')
        self.login_page.click_btn_logout()
        sleep(3)
        # 登出后，"退出登录"变为"立即登录"
        text_change = self.login_page.show_text_change()
        # 判断登出是否成功
        self.assertEqual(text_change, "立即登录", msg="登出失败")

    def test_02(self):
        u'''密码登录测试'''
        self.login_page = LoginPage(self.driver)
        self.login_page.open_login_page()
        self.login_page.choose_tab_password()
        self.login_page.input_username(self.username)
        self.login_page.input_password(self.password)
        self.login_page.click_btn_login_pwd()
        # 等待时间后续优化
        sleep(3)
        user_id = self.login_page.show_user_id()
        # 判断登录是否成功
        self.assertEqual(user_id, self.expect_user_id, msg='登录失败')
        self.login_page.click_btn_logout()
        sleep(3)
        # 登出后，"退出登录"变为"立即登录"
        text_change = self.login_page.show_text_change()
        # 判断登出是否成功
        self.assertEqual(text_change, "立即登录", msg="登出失败")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
