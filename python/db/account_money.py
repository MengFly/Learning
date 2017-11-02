# encoding:utf-8
'''
Created on 2017年1月16日

@author: mengfei

数据库操作模仿银行转账业务
'''
import sys
import MySQLdb
from model1.db_config import host, user, port, passwd, db, charset

class TransferMoney(object):
    def __init__(self, conn):
        self.conn = conn
    
    # 检查用户是否存在
    def check_acct_available(self, acctid):
        cursor = self.conn.cursor()
        try:
            sql = "select * from account where acctid=%s" %acctid
            cursor.execute(sql)
            print("check_acct_available" + sql)
            rs = cursor.fetchall()
            if len(rs) != 1 :
                raise Exception("账号%s不存在"%acctid)
        finally:
            cursor.close()
    
    # 检查转账者是否有足够的钱
    def has_enough_money(self, acctid, money):
        cursor = self.conn.cursor()
        try:
            sql = "select * from account where acctid=%s and money >= %s" %(acctid,money)
            cursor.execute(sql)
            print("has_enough_money" + sql)
            rs = cursor.fetchall()
            if len(rs) != 1 :
                raise Exception("账号%s余额不足"%acctid)
        finally:
            cursor.close()
    
    
    # 减少钱
    def reduce_money(self, acctid, money):
        cursor = self.conn.cursor()
        try:
            sql = "update account set money=money-%s where acctid=%s" %(money,acctid)
            cursor.execute(sql)
            print("reduce_money" + sql)
            if cursor.rowcount != 1 :
                raise Exception("账号%s减款失败"%acctid)
            else :
                print("账号%s付款%s成功"%(acctid, money))
        finally:
            cursor.close()
    
    # 增加钱
    def add_money(self, acctid, money):
        cursor = self.conn.cursor()
        try:
            sql = "update account set money=money + %s where acctid=%s" %(money,acctid)
            cursor.execute(sql)
            print("reduce_money" + sql)
            if cursor.rowcount != 1 :
                raise Exception("账号%s加款失败"%acctid)
            else :
                print("账号%s收款%s成功"%(acctid, money))
        finally:
            cursor.close()
        
    # 转账逻辑
    def transfer(self, source_acctid, target_acctid, money):
        try :
            self.check_acct_available(source_acctid)
            self.check_acct_available(target_acctid)
            self.has_enough_money(source_acctid, money)
            self.reduce_money(source_acctid, money)
            self.add_money(target_acctid, money)
            self.conn.commit()
            print("转账成功")
        except Exception as e:
            self.conn.rollback()
            raise e # 把异常重新抛出

if __name__ == "__main__":
    # 付款人
    source_acctid = sys.argv[1]
    # 收款人
    target_acctid = sys.argv[2]
    # 金额
    money = sys.argv[3]
    
    conn = MySQLdb.connect(host=host, user=user, port = port, 
                           passwd = passwd, db = db, charset=charset)
    tr_money = TransferMoney(conn)
    
    try :
        tr_money.transfer(source_acctid, target_acctid, money)
    except Exception as e:
        print("出现问题" + str(e))
    finally :
        conn.close()