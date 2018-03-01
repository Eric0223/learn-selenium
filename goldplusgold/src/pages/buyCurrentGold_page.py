# -*- coding:utf-8 -*-
'''
Created on 2017-12-11
@author: luox
description: 流动金页面
'''
from src.common.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait


class BuyCurrentGold(BasePage):
    # 流动金买入按钮
    btn_current = ("class name", "u-btn")
    # 按克数购买
    tab_by_grams = ("xpath", ".//*[@id='bodys']/div[3]/div/div[1]/ul[2]/li[1]/ul/li[1]")
    # 按金额购买
    tab_by_money = ("xpath", ".//*[@id='bodys']/div[3]/div/div[1]/ul[2]/li[1]/ul/li[2]")
    # 输入购买克数
    input_grams_loc = ("id", "num1")
    # 输入购买金额
    input_money_loc = ("id", "price2")
    # 买入按钮
    btn_buy = ("css selector", ".u-btn.buyBtn")
    # 下一步
    btn_next = ("class name", "payBtn")
    # 选择支付方式,余额支付
    by_balance = ("id", "balance")
    # 交易密码输入框
    trading_password_loc = ("id", "walletPaddword")
    # 立即支付
    btn_pay_immediately = ("css selector", ".immdeiatePay.u-btn.walletBtn")
    # 选择支付方式,银行卡支付
    by_bankcard = ("class name", "bankCardName")

    def __init__(self, driver, buygold_url="http://qa.hjb.com/buyGoldList.html",
                 buygold_title="中国黄金金有金-产品列表-期限灵活"):
        BasePage.__init__(self, driver, buygold_url, buygold_title)

    # 打开买金页面
    def open_currentGold_page(self):
        self._open(self.url, self.page_title)

    # 点击立即买入流动金
    def click_btn_currentGold(self):
        self.find_element(*self.btn_current).click()

    # 购买方式：按克重购买
    def buy_by_grams(self):
        self.find_element(*self.tab_by_grams).click()

    # 购买方式：按金额购买
    def buy_by_money(self):
        self.find_element(*self.tab_by_money).click()

    # 输入克数
    def input_grams(self, grams):
        self.send_keys(grams, *self.input_grams_loc)

    # 输入金额
    def input_money(self, amount):
        self.send_keys(amount, *self.input_money_loc)

    # 点击买入按钮
    def click_btn_buy(self):
        self.find_element(*self.btn_buy).click()

    # 点击下一步
    def click_btn_next(self):
        self.find_element(*self.btn_next).click()

    # 支付方式为余额支付
    def pay_by_balance(self):
        self.find_element(*self.by_balance).click()

    # 支付方式为快捷支付
    def pay_by_bankcard(self):
        self.find_element(*self.by_bankcard).click()

    # 输入交易密码
    def input_trading_password(self, trading_password):
        self.send_keys(trading_password, *self.trading_password_loc)

    # 点击立即支付
    def click_btn_pay_immediately(self):
        self.find_element(*self.btn_pay_immediately).click()


