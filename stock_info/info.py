# 确保脚本可以直接执行
import os,sys
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(root_dir)

import tushare as ts
from types import *
import pandas as pd
from stock_info.conf import token

class Client:
    api = ts.pro_api(token)

    def basic(self) -> pd.DataFrame:
        return Client.api.stock_basic()

    def daily(self,ts_code:str, trade_date:str, start_date:int, end_date:int) -> pd.DataFrame:
        return Client.api.daily(**{
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


cli = Client(token)
df = cli.daily()

print(df.count())