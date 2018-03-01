# -*- coding:utf-8 -*-
'''
Created on 2017-12-11
@author: luox
description:登录页
'''

from src.common.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage(BasePage):
    # 快捷登录
    tab_quick = ("xpath", ".//*[@id='bodys']/div[3]/div[2]/div[1]/div[3]")
    phone_loc = ("id", "shortcut-iphone")
    btn_verifyCode_loc = ("class name", "Verification-countdown")
    verify_code_loc = ("id", "code")
    btn_login_loc = ("css selector", ".loginBtn.short-message")

    # 密码登录
    tab_password = ("xpath", ".//*[@id='bodys']/div[3]/div[2]/div[1]/div[4]")
    username_loc = ("id", "iphone")
    password_loc = ("class name", "password")
    link_forgot_pwd = ("link text", "忘记密码")
    btn_login_loc2 = ("css selector", ".loginBtn.password-login")
    test_id_loc = ("class name", "register")
    # 登录成功后首页退出登录按钮
    btn_logout_loc = ("css selector", ".singIn.logOut")
    # 登出成功后首页退出登录变为立即登录
    text_change = ("class name", "singIn")

    def __init__(self, driver, login_url="http://qa.hjb.com/login.html",
                 login_title="中国黄金金有金-登录-互联网黄金理财首选"):
        BasePage.__init__(self, driver, login_url, login_title)

    # 打开登录页面
    def open_login_page(self):
        self._open(self.url, self.page_title)

    # 选择快捷登录
    def choose_tab_quick(self):
        self.find_element(*self.tab_quick).click()

    # 输入手机号
    def input_phone(self, phone):
        self.send_keys(phone, *self.phone_loc)

    # 获取验证码
    def get_verify_code(self):
        self.find_element(*self.btn_verifyCode_loc).click()

    # 输入验证码
    def input_verify_code(self, code):
        self.send_keys(code, *self.verify_code_loc)

    # 点击登录（快捷登录）
    def click_btn_login(self):
        self.find_element(*self.btn_login_loc).click()

    # 选择密码登录
    def choose_tab_password(self):
        self.find_element(*self.tab_password).click()

    # 输入用户名
    def input_username(self, username):
        self.send_keys(username, *self.username_loc)

    # 输入密码
    def input_password(self, password):
        self.send_keys(password, *self.password_loc)

    # 点击登录（密码登录）
    def click_btn_login_pwd(self):
        self.find_element(*self.btn_login_loc2).click()

    # 忘记密码
    def forgot_password(self):
        self.find_element(*self.link_forgot_pwd).click()

    # 登录成功userID查找
    def show_user_id(self):
        return self.find_element(*self.test_id_loc).text

    # 退出登录
    def click_btn_logout(self):
        self.find_element(*self.btn_logout_loc).click()

    # 登出成功，退出登录变为立即注册
    def show_text_change(self):
        return self.find_element(*self.text_change).text
