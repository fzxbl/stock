import os

_root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONF_DIR = os.path.join(_root_dir, 'conf')
LOG_DIR = os.path.join(_root_dir, 'logs')
