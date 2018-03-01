# -*- coding:utf-8 -*-
'''
Created on 2017-12-11
@author: luox
Project:
'''
import time
import os
from selenium import webdriver

# 获取项目路径
# project_path = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)[0]), '.'))
project_path = os.path.abspath(
    os.path.join(
        os.path.dirname(
            os.path.split(
                os.path.realpath(__file__))[0]),
        '.'))
# 测试用例代码存放路径（用于构建suite,注意该文件夹下的文件都应该以test开头命名）
test_case_path = project_path + "\\src\\test_case"
# excel测试数据文档存放路径
test_data_path = project_path+"\\data\\testData.xlsx"
# 日志文件存储路径
log_path = project_path+"\\log\\mylog.log"
img_path = project_path + "\\error_img\\"
report_path = project_path + "\\report\\"  # 测试报告存储路径，并以当前时间作为报告名称前缀
# report_name = report_path+time.strftime('%Y%m%d%H%S', time.localtime())
report_name = report_path + time.strftime("%Y%m%d_%H%M%S")

# 设置发送测试报告的公共邮箱、用户名和密码
smtp_sever = "smtphz.qiye.163.com"  # 邮箱SMTP服务
email_name = "luoxiao@zjhjb.com"  # 发件人
email_password = "lx19920223!"  # 发件人登录密码
email_To = "luoxiao@zjhjb.com"  # 收件人

# 配置文件地址
profile_directory = r'C:\Users\Administrator\AppData\Local\Temp\tmp8o70rh\webdriver-py-profilecopy'
# 加载配置
profile = webdriver.FirefoxProfile(profile_directory)
