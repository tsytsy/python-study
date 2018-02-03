#!/usr/bin/env python
# _*_ coding:utf8 _*_

import configparser

conf = configparser.ConfigParser()
conf.read('host_info.conf')
print(conf.options('group 1'))
