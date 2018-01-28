#!/usr/bin/env python
# _*_ coding:utf8 _*_
from core import service
from conf import common
from core import reg_login
from core import service
import socket
import struct
import hashlib
import json


class start(reg_login.reg_login):
    def __init__(self, server_address):
        self.server_address = server_address
        common.my_sock.__init__(self, server_address)
        self.begin()
    def begin(self):
        menu = '''
        1. 注册
        2. 登录
        q. 退出
        '''
        menu_dic = {
            '1': self.register,
            '2': self.login,
            'q': self.quit_menu
        }
        while True:
            print(menu)
            choose = input('>>:')
            if choose in menu_dic:
                menu_dic[choose]()
            else:
                print('输入错误，请重新选择服务')

    def register(self):     # 可以在此函数中进行拓展
        print('register')
        username = input('注册用户名>>:')
        passwd = input('注册用户密码>>:')
        super(start, self).register(username, passwd)
        self.reg_recvfrom_server()

    def login(self):    # 可以在此函数中进行拓展
        username = input('username>>:')
        passwd = input('passwd>>:')
        print('#######')
        super(start, self).login(username, passwd)

        num = self.login_recvfrom_server()
        if num == 2:
            self.service = service.Service(self.server_address, username)
            self.service.run()

    def quit_menu(self):
        exit()

