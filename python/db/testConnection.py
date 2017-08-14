# encoding=utf-8
'''
Created on 2017年1月16日

@author: mengfei
'''
import MySQLdb
import db_config


def testSelect(conn, cursor):   
    sql  = 'select * from user'
    cursor.execute(sql)
    # 这个时候本地缓冲区中已经有了数据
    print cursor.rowcount
    
    # 获取一条数据
    rs = cursor.fetchone()
    print rs
    
    # 获取三条数据
    rs = cursor.fetchmany(3)
    print rs
    
    # 获取剩下的所有数据
    rs = cursor.fetchall()
    
    print rs

# 获取数据库连接
def testSelect2(conn, cursor):
    sql = "select * from user"
    cursor.execute(sql)
    rs = cursor.fetchall()
    for row in rs :
        print "userId = %s ==> userName = %s" %row
def testiud(conn, cursor):
    sql_insert = "insert into user(id, username) values(default, 'name10')"
    sql_update = "update user set username='小明' where id = 4"
    sql_delete = "delete from user where id < 3"
    try :
        cursor.execute(sql_insert)
        print cursor.rowcount
        cursor.execute(sql_update)
        print cursor.rowcount
        cursor.execute(sql_delete)
        print cursor.rowcount
        # 因为MySQLdb默认关闭了自动提交，所以如果没有conn.commit()的话所有操作将不会生效
        conn.commit()
    except Exception as e:
        print e
        # 如果出现异常那么久进行数据回滚
        conn.rollback()
        


conn = MySQLdb.Connect(
        host = db_config.host,        
        port = db_config.port,
        user = db_config.user,
        passwd = db_config.passwd,
        db = db_config.db,
        charset = db_config.charset
    )

cursor = conn.cursor()

# testSelect
testSelect(conn, cursor)
# testSelect2
testSelect2(conn, cursor)
# testuid
testiud(conn, cursor)



cursor.close()
conn.close()

