#!/usr/bin/env python
# _*_ coding:utf8 _*_
import hashlib
import socket
import struct
import json
from conf import common

class reg_login(common.my_sock):

    def register(self, username, passwd):
        self.username_passwd_transfer('register', username, passwd)

    def login(self, username, passwd):
        self.username_passwd_transfer('login', username, passwd)

    def reg_recvfrom_server(self):
        num = self.socket.recv(4)[0]
        if num == 1:
            print('注册成功')
        if num == 0:
            print('用户名存在，请重新注册')

    def login_recvfrom_server(self):
        num = self.socket.recv(4)[0]
        if num == 2:
            print('登录成功')
        if num == 1:
            print('账号或者密码错误')
        if num == 0:
            print('此账号不存在，请重新登录')
        return num

    def username_passwd_transfer(self, type, username, passwd):
        passwd_md5_obj = hashlib.md5()
        passwd_md5_obj.update(passwd.encode('utf-8'))
        passwd_md5 = passwd_md5_obj.hexdigest()
        reg_dic = {'cmd': type, 'username': username, 'passwd': passwd_md5}
        reg_dic_bytes = common.dic_to_bytes(reg_dic)
        head_struct = struct.pack('i', len(reg_dic_bytes))  # 4bytes数据表示reg_dic的长度，如80
        self.socket.send(head_struct)
        self.socket.send(reg_dic_bytes)
