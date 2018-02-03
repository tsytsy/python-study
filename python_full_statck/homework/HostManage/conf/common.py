#!/usr/bin/env python
# _*_ coding:utf8 _*_
import configparser
from conf import settings
import json

conf = configparser.ConfigParser()
conf.read(settings.HOST_CONF_DIR)

def section_list():
    sect_list = conf.sections()
    return sect_list

def opition_list(group):
    opt_list = conf.items(group)
    return opt_list


def read_group_info_dic(group):
    groupmember_info = []
    for host in conf.options(group):
        host_str = conf.get(group, host)
        host_dic = json.loads(host_str)
        groupmember_info.append(host_dic)
    return groupmember_info

