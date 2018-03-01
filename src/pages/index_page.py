# -*- coding:utf-8 -*-
'''
Created on 2017/12/12 18:41
@author: luox
description:首页
'''
from src.common.base_page import BasePage


class IndexPage(BasePage):
    # 立即登录
    btn_login_loc = ("class name", "singIn")
    # 免费注册
    btn_register_loc = ("link text", "免费注册")
    # 注册领万元本金
    btn_register2_loc = ("css selector", ".pBtn.u-btn")
    # 首页
    link_index_loc = ("link text", "首页")
    # 买入黄金
    link_buygold_loc = ("link text", "买入黄金")
    # 黄金账户
    link_account_loc = ("link text", "黄金账户")
    # 关于我们
    link_about_loc = ("link text", "关于我们")
    # 金价走势
    link_goldtrend_loc = ("link text", "金价走势>")

    def __init__(self, driver, index_url="http://qa.hjb.com",
                 index_title="中国黄金·金有金-我的黄金管家"):
        BasePage.__init__(self, driver, index_url, index_title)

    # 打开首页
    def open_index_page(self):
        self._open(self.url, self.page_title)

    # 点击立即登录
    def click_btn_login(self):
        self.find_element(*self.btn_login_loc).click()

    # 点击免费注册
    def click_btn_register(self):
        self.find_element(*self.btn_register_loc).click()

    # 点击注册领万元本金
    def click_btn_register_experence(self):
        self.find_element(*self.btn_register2_loc).click()

    # 点击“首页”
    def click_index(self):
        self.find_element(*self.link_index_loc).click()

    # 点击“买入黄金”
    def click_buy_gold(self):
        self.find_element(*self.link_buygold_loc).click()

    # 点击“黄金账户”
    def click_gold_account(self):
        self.find_element(*self.link_account_loc).click()

    # 点击“关于我们”
    def click_about_us(self):
        self.find_element(*self.link_about_loc).click()

    # 点击“金价走势”
    def click_goldtrend(self):
        self.find_element(*self.link_goldtrend_loc).click()
