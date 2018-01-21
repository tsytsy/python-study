import logging
import sys
import os
from conf import settings
sys.path.append(settings.BASE_DIR)
def logger(log_type):
    logger = logging.getLogger()
    fm = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
    file_path = os.path.join(settings.BASE_DIR, 'log', settings.LOG_TYPES[log_type])
    # print(file_path)
    fh = logging.FileHandler(file_path)
    # sh = logging.StreamHandler()
    fh.setFormatter(fm)
    # sh.setFormatter(fm)
    logger.addHandler(fh)
    # logger.addHandler(sh)
    logger.setLevel(10)
    return logger
