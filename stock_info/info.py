# 确保脚本可以直接执行
import os,sys
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(root_dir)

import tushare as ts
from types import *
import pandas as pd
from stock_info.conf import token

class Client:
    _api = ts.pro_api(token)

    def stock_list(self) -> pd.DataFrame:
        try:
            stocks = Client._api.stock_basic()
        except Exception as e:
            return 
        return stocks

    def daily(self,ts_code:str, trade_date:str, start_date:int, end_date:int) -> pd.DataFrame:
        return Client._api.daily(**{
            "ts_code": ts_code,
            "trade_date":trade_date,
            "start_date": start_date,
            "end_date": end_date,
            "offset": "",
            "limit": ""
        }, fields=[
            "ts_code",
            "trade_date",
            "open",
            "high",
            "low",
            "close",
            "pre_close",
            "change",
            "pct_chg",
            "vol",
            "amount"
        ])

    def dump2db(self, df:pd.DataFrame, table:str):
        df.to_sql

cli = Client()
df = cli.daily('000157.SZ','',20230622,20230623)

print(df.empty)
print(df)