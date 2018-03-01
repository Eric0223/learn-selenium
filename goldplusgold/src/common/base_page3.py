# -*- coding:utf-8 -*-
'''
Created on 2017-12-11
@author: luox
description:封装页面公用方法
'''
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.common import log
from config.globalparameter import img_path
from selenium import webdriver


class BasePage(object):
    def __init__(self, driver, base_url, page_title):
        self.driver = driver
        self.url = base_url
        self.title = page_title
        # self.mylog = log.log()

    # 打开页面,并校验链接是否加载正确
    def _open(self, url, page_title):
        try:
            self.driver.get(url)
            self.driver.maximize_window()
            # 通过断言输入的title是否在当前title中
            assert page_title in self.driver.title, u'打开页面失败：%s' % url
        except BaseException:
            self.mylog.error(u'未能正确打开页面:' + url)

    # 重写find_element方法，增加定位元素的健壮性
    def find_element(self, *loc):
        try:
            WebDriverWait(
                self.driver, 10).until(
                EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except BaseException:
            self.mylog.error(u'找不到元素:' + str(loc))

    # 重写send_keys方法
    def send_keys(self, value, clear=True, *loc):
        try:
            if clear:
                self.find_element(*loc).clear()
                self.find_element(*loc).send_keys(value)
        except AttributeError:
            self.mylog.error(u'输入失败,loc=' + str(loc) + u';value=' + value)

    # 截图
    def img_screen_shot(self, img_name):
        try:
            self.driver.get_screenshot_as_file(img_path + img_name + '.png')
        except BaseException:
            self.mylog.error(u'截图失败：' + img_name)
