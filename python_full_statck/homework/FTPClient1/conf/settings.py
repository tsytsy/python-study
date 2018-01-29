#!/usr/bin/env python
# _*_ coding:utf8 _*_
import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)

# SERVER_ADDRESS = ('127.0.0.1', 9004)
SERVER_ADDRESS = ('192.168.1.66', 9004)
RECV_BASE_DIR = os.path.join(BASE_DIR, 'file_download')

