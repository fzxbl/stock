# 确保脚本可以直接执行
import os,sys
_root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(_root_dir)

import tushare as ts
from types import *
import pandas as pd

from config import conf_parse
from database import db
from log import  ilogging




class Client:
    def __init__(self, token:str):
        self._api = ts.pro_api(token)
        self._db_session = db.init_mysql_by_conf('stock_db.toml')
        self._logger = ilogging.init_looger_by_conf('stock_logger.json', 'base')

    def stock_list(self) -> pd.DataFrame:
        try:
            stocks = self._api.stock_basic()
        except Exception as e:
            return 
        return stocks

    def daily(self,ts_code:str, trade_date:str, start_date:int, end_date:int) -> pd.DataFrame|None:
        p = locals()
        try:
            df = self._api.daily(**{
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
        except Exception as e:
            self._logger.error("request fail, %s", e)
        if df.empty:
            self._logger.warn("no data found, ", p)
            return None
        return df

    def dump2db(self, df:pd.DataFrame, table:str):
        res = df.to_sql(table, self._db_session, index=False, if_exists='append', chunksize=5000)
        if res is None:
            self._logger.warning('dump2db failed')

if __name__ == '__main__':
    token = conf_parse.load_toml_config('stock_auth.toml')['token']
    cli = Client(token)
    df = cli.daily('000157.SZ','',20230615,20230623)
    print(df.empty)
    print(df)

