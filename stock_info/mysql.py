'''
Created on 2020年1月30日

@author: JM
'''
import pandas as pd
import tushare as ts
from sqlalchemy import create_engine 

# engine_ts = create_engine('mysql://user:mima@127.0.0.1:3306/demos?charset=utf8&use_unicode=1')

def read_data():
    sql = """SELECT * FROM stock_basic LIMIT 20"""
    df = pd.read_sql_query(sql, engine_ts)
    return df


def write_data(df):
    res = df.to_sql('stock_basic', engine_ts, index=False, if_exists='append', chunksize=5000)
    print(res)


def get_data():
    pro = ts.pro_api('cb2b2e2aff5b81d4f9e60d0fd9daaf5f983b09254b8108877bce6197')
    df = pro.stock_basic()
    return df


if __name__ == '__main__':
#     df = read_data()
    df = get_data()
    # write_data(df)
    print(df)