#!/usr/bin/env python
# _*_ coding:utf8 _*_

import os, sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.insert(0, BASE_DIR)
from core import main

if __name__ == '__main__':
    t = main.HostManage()
