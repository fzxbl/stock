import toml
import sys,os
from types import *

# 确保脚本可以直接执行
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(root_dir)

from env import CONF_DIR

def load_toml_config(conf_name:str) -> any:
    cfg = toml.load(os.path.join(CONF_DIR, conf_name))
    return cfg


if __name__ == '__main__': 
    cfg = load_toml_config('stockauth.toml')
    print(cfg)