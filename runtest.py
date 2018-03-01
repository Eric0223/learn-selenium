# coding:utf-8
'''
Created on 2018/2/1 13:41
@author: luox
description: 执行测试
'''
import sys
import unittest
import time
import HTMLTestRunner_jpg
from config.globalparameter import test_case_path, report_name
from src.common import send_mail
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append('./interface')


# 构建测试集,包含src/test_case目录下的所有以test开头的.py文件
suite = unittest.defaultTestLoader.discover(
    start_dir=test_case_path, pattern='test*.py')

# 执行测试
if __name__ == "__main__":
    report = report_name + "Report.html"
    fb = open(report, 'wb')
    runner = HTMLTestRunner_jpg.HTMLTestRunner(
        stream=fb,
        title=u'金有金-PC自动化测试报告',
        description=u'项目描述：qa环境',
        retry=1 # 用例失败重跑次数
    )
    runner.run(suite)
    # 关闭文件
    fb.close()

    # 发送邮件
    time.sleep(10)  # 设置睡眠时间，等待测试报告生成完毕
    email = send_mail.send_email()
    email.sendReport()
