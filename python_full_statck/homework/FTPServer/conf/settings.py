#!/usr/bin/env python
# _*_ coding:utf8 _*_

import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)
HOME_DIR = os.path.join(BASE_DIR, 'home')
DB_USER_DIR = os.path.join(BASE_DIR, 'db', 'user')
SERVER_ADDRESS = ('127.0.0.1', 9004)
# SERVER_ADDRESS = ('192.168.1.66', 9004)
FILE_MAX_SIZE_LEVEL0 = 100000000    # 100M
FILE_MAX_SIZE_LEVEL1 = 500000000    # 100M