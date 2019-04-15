import os.path
from pprint import pprint

import pandas as pd
import pymysql.cursors


def get_mysql_connect():
    return pymysql.Connect(host="localhost", port=3306,
                           user="root", passwd="",
                           db="survey-data", charset="utf8")


def get_data_file_list():
    top_dir = r"D:/dfcode"
    for _, _, files in os.walk(top_dir):
        return [os.path.join(top_dir, item) for item in files]


def save_item_to_db(loc, cursor):
    sql = r"INSERT zzbz_s_jd011dm (code, name, cxfldm) VALUES ('%s', '%s', '%s')" % (loc[0], loc[1], loc[2])
    cursor.execute(sql)


def save_to_db(data_file, cursor):
    if os.path.exists(data_file):
        df = pd.read_csv(data_file, engine="python", encoding="utf-8")
        one_total = len(df.index)
        for index in df.index:
            loc = df.loc[index]
            save_item_to_db(loc, cursor)
            if index % 100 == 0:
                pprint("已完成%d/%d" % (index, one_total))
    else:
        pprint("文件不存在")


if __name__ == '__main__':
    connect = get_mysql_connect()
    cursor = connect.cursor()
    data_file_list = get_data_file_list()
    try:
        for data_file in data_file_list:
            pprint("处理文件：" + str(data_file))
            save_to_db(data_file, cursor)
    finally:
        connect.commit()
        cursor.close()
        connect.close()
