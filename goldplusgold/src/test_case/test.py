# -*- coding:utf-8 -*-
'''
Created on 2018/2/23 16:49
@author: luox
Description:
'''
import sys
import logging
reload(sys)
sys.setdefaultencoding('utf-8')


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, # 日志级别设置
    format="%(asctime)s %(filename)s [line: %(lineno)d] %(levelname)s %(message)s",
    datefmt='%a, %d %b %Y %H:%M:%S', filename='mylog.log',
    filemode='w')
    ###################################################
    # 定义一个StreamHandler，将info级别的或更高级别的日志输出到标错错误
    # 并将其添加到当前的日志处理对象
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)
    ###################################################
    logging.debug(u"这是debug日志记录")
    logging.info(u'这是info日志记录')
    logging.warning(u'这是warning日志记录')
