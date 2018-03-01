# -*- coding:utf-8 -*-
'''
Created on 2017/12/13 21:54
@author: luox
Description: 数据库操作
'''
import pymysql


class DatabaseOperation(object):
    # 连接配置信息
    config = {
        'host': 'goldmysql.hjb.com',
        'user': 'hjb2018',
        'password': 'hjb150601',
        'db': 'gold_treasure_qa',
        'charset': 'utf8',
        'cursorclass': pymysql.cursors.DictCursor,
    }
    # 创建连接
    db = pymysql.connect(**config)

    # 查询操作
    def get_data(self, key, sql):
        # 使用cursor()方法获取操作游标
        cur = self.db.cursor()
        try:
            cur.execute(sql)
            # 获取所有记录列表
            results = cur.fetchall()
            for row in results:
                data = row[key]
                return data
        except Exception as e:
            raise e
        self.db.close()

    # 插入操作
    def insert_data(self, sql_insert):
        cur = self.db.cursor()
        try:
            cur.execute(sql_insert)
            self.db.commit()
            print("************数据插入成功************\n")
        except Exception as e:
            self.db.rollback()
            raise e
        finally:
            self.db.close()

    # 更新操作
    def update_data(self, sql_update):
        cur = self.db.cursor()
        try:
            cur.execute(sql_update)
            self.db.commit()
            print("************数据更新成功************\n")
        except Exception as e:
            self.db.rollback()
            raise e
        finally:
            self.db.close()

    # 删除操作
    def delete_data(self, sql_delete):
        cur = self.db.cursor()
        try:
            cur.execute(sql_delete)
            self.db.commit()
            print("************数据删除成功************\n")
        except Exception as e:
            self.db.rollback()
            raise e
        finally:
            self.db.close()



