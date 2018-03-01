# -*- coding:utf-8 -*-
'''
Created on 2017/12/21/021 23:28
@author: luox
Description:
'''
from src.common.base_page import BasePage


class BuyRegularGold(BasePage):
    btn_regular_30days = ("xpath", ".//*[@id='bodys']/div[3]/div[3]/ul/li[1]/div[5]/div/a")
    btn_regular_60days = ("xpath", ".//*[@id='bodys']/div[3]/div[3]/ul/li[2]/div[5]/div/a")
    btn_regular_90days = ("xpath", ".//*[@id='bodys']/div[3]/div[3]/ul/li[3]/div[5]/div/a")
    btn_regular_180days = ("xpath", ".//*[@id='bodys']/div[3]/div[3]/ul/li[4]/div[5]/div/a")
    btn_regular_365days = ("xpath", ".//*[@id='bodys']/div[3]/div[3]/ul/li[5]/div[5]/div/a")

    # 点击立即买入传家金30天
    def click_btn_buy30days(self):
        self.find_element(*self.btn_regular_30days).click()

    # 点击立即买入传家金60天
    def click_btn_buy60days(self):
        self.find_element(*self.btn_regular_60days).click()

    # 点击立即买入传家金90天
    def click_btn_buy90days(self):
        self.find_element(*self.btn_regular_90days).click()

    # 点击立即买入传家金180天
    def click_btn_buy180days(self):
        self.find_element(*self.btn_regular_180days).click()

    # 点击立即买入传家金365天
    def click_btn_buy365days(self):
        self.find_element(*self.btn_regular_365days).click()