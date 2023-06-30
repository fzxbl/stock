import loguru
import os,sys,json5,json
_root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(_root_dir)

from env import LOG_DIR, CONF_DIR

def _serialize(record):
    subset = {
        "time": record["time"].strftime("%Y-%m-%d %H:%M:%S"),
        "message": record["message"],
        "level": record["level"].name,
        "pos":record["file"].path + ":" + str(record["line"]),
        "func":record["function"],
    }
    return json.dumps(subset)

def _patching(record):
    record["extra"]["serialized"] = _serialize(record)




def init_logger_by_conf(conf_name:str) -> loguru.logger:
    logger = loguru.logger
    log_config_dict = {}
    with open(os.path.join(CONF_DIR, conf_name), 'r') as f:
        log_config_dict = json5.load(f)
    for handler in log_config_dict['handlers']:
        # 处理宏替换
        handler['sink'] = handler['sink'].format_map({'LOG_DIR':LOG_DIR})
        # 处理sink为console的情况
        if handler['sink'] == 'console':
            handler['sink'] = sys.stdout
        else:
            handler['colorize'] = False
        # 处理json日志输出
        if handler['serialize']:
            handler['format'] = '{extra[serialized]}'
            handler['serialize'] = False
    logger.configure(**log_config_dict)
    logger = logger.patch(_patching)
    return logger




if __name__ == "__main__":
    logger = init_logger_by_conf('stock_logger2.json')
    a = 5
    b = 0
    try:
        a/b
    except Exception as e:
        logger.exception(e)
    