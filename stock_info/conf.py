import toml
import sys,os

# 确保脚本可以直接执行
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(root_dir)

from env import CONF_DIR

_cfg = toml.load(CONF_DIR+ "/auth.toml")
token = _cfg["token"]


if __name__ == '__main__': 
    print(_cfg)