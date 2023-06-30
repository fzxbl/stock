import logging.config
import os,json5,sys

_root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(_root_dir)
from env import LOG_DIR, CONF_DIR

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)


def init_looger_by_conf(conf_name:str, logger_name:str) -> any:
    log_config_dict = {}
    with open(os.path.join(CONF_DIR, conf_name), 'r') as f:
        log_config_dict = json5.load(f)
        handlers = log_config_dict['handlers']
        for cfg in handlers.values():
            for k, v in cfg.items():
                if k == 'filename':
                    v = v.format_map({'LOG_DIR':LOG_DIR})
                    cfg[k] = v

    logging.config.dictConfig(log_config_dict)
    logger = logging.getLogger(logger_name)
    return logger

if __name__ == '__main__':
    logger1 = init_looger_by_conf('logger.json', 'base')
    logger1.info("asdf")
   