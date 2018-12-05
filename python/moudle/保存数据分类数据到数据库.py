import pandas as pd
import pymysql.cursors


def get_mysql_connect():
    return pymysql.Connect(host="localhost", port=3306,
                           user="root", passwd="",
                           db="survey-data", charset="utf8")


def read_excel_content():
    return pd.read_excel("data.xls", converters={"门类": str, "大类": str, "种类": str, "小类": str, "类别名称": str, "说明": str})


def save_loc_to_db(index, loc, connect):
    print(index, " save ", loc)
    insert_sql = r"INSERT INTO zzbz_s_gmjjhyfl (id, ml, dl, zl, xl, lbmc, sm) VALUES ( '%d', '%s', '%s','%s','%s','%s','%s')"
    data = (index, loc[r"门类"], loc[r"大类"], loc[r"种类"], loc[r"小类"], loc[r"类别名称"], loc[r"说明"])
    sql = insert_sql % data
    connect.cursor().execute(sql)
    connect.commit()


if __name__ == '__main__':
    data = read_excel_content()
    connect = get_mysql_connect()
    try:
        for index in data.index:
            loc = data.loc[index]
            save_loc_to_db(index, loc, connect)
    finally:
        connect.close()
