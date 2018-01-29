#!/usr/bin/env python
# _*_ coding:utf8 _*_

#!/usr/bin/env python
# _*_ coding:utf8 _*_
import time
import socketserver
import struct
import json
import os
import logging
import hashlib
import subprocess
from conf import settings
from conf import common

def Mylogger():
    logger = logging.getLogger()
    fm = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
    file_path = os.path.join('file_load', 'receive.txt')
    # print(file_path)
    fh = logging.FileHandler(file_path)
    sh = logging.StreamHandler()
    fh.setFormatter(fm)
    sh.setFormatter(fm)
    logger.addHandler(fh)
    logger.addHandler(sh)
    logger.setLevel(10)
    return logger


class FTPSERVER(socketserver.BaseRequestHandler):
    def handle(self):
        print(self.client_address, 'connected')
        while True:     # 服务端根据字典里的
            head_len = struct.unpack('i', self.request.recv(4))[0]
            head_bytes = self.request.recv(head_len)
            head_json = head_bytes.decode('utf-8')
            head_dict = json.loads(head_json)
            print(head_dict)

            cmd = head_dict['cmd']
            if hasattr(self, cmd):
                func = getattr(self, cmd)
                func(head_dict)
            else:
                break

    def put(self, head_dict):
        # logger = Mylogger()
        recv_md5_file = hashlib.md5()
        BASE_DIR1 = os.path.join(settings.HOME_DIR, self.username)
        if not os.path.exists(BASE_DIR1):
            os.mkdir(BASE_DIR1)
        file_name = os.path.join(BASE_DIR1, head_dict['filename'])
        file_size = head_dict['filesize']

        dir_size = common.getdirsize(BASE_DIR1)
        print('********', file_size, '\t', dir_size)
        if dir_size + file_size > self.homedir_size:
            put_feedback_bytes = struct.pack('i', 0)
            self.request.send(put_feedback_bytes)
            return
        else:
            put_feedback_bytes = struct.pack('i', 1)
            self.request.send(put_feedback_bytes)
        f = open(file_name, 'wb')
        recv_size = 0
        while recv_size < file_size:
            minus = file_size - recv_size
            if minus > 1024:
                size = 1024
            else:
                size = minus
            data = self.request.recv(size)
            f.write(data)
            recv_md5_file.update(data)
            recv_size += len(data)
            # log = 'from {} the size is {}'.format(self.client_address, recv_size)
            # print(log)
            # logger.debug(log)
        print('put finish')
        recv_md5 = recv_md5_file.hexdigest()
        send_md5 = self.request.recv(32)
        print('recv md5 is:', recv_md5)
        if recv_md5 == send_md5.decode('utf-8'):
            print('收到的文件与接收的文件一致')
            issame_bytes = struct.pack('i', 1)
        else:
            print('收到的文件与源文件不一致，删除请重传')
            issame_bytes = struct.pack('i', 0)
            os.remove(file_name)
        f.close()
        self.request.send(issame_bytes)

    def get(self, head):
        print('get..........')
        BASE_DIR = os.path.join(settings.HOME_DIR, self.username)
        file_name = os.path.join(BASE_DIR, head['filename'])
        if not os.path.exists(file_name):
            print(file_name)
            res = struct.pack('i', 0)
            self.request.send(res)
            return
        data_size = os.path.getsize(file_name)
        head_dic = {'filename': os.path.basename(file_name), 'datasize': data_size}
        print('====================>')
        head_json = json.dumps(head_dic)
        head_bytes = head_json.encode('utf-8')
        res = struct.pack('i', len(head_bytes))
        print(res)

        self.request.send(res)
        self.request.send(head_bytes)
        f = open(file_name, 'rb')
        send_bytes = 0
        send_md5_obj = hashlib.md5()
        for line in f:
            self.request.send(line)
            send_md5_obj.update(line)
            send_bytes += len(line)
            print(send_bytes)
        f.close()
        print('send finish')
        send_md5_str = send_md5_obj.hexdigest()
        print('发送：', send_md5_str)
        send_md5_bytes = bytes(send_md5_str, encoding='utf-8')
        self.request.send(send_md5_bytes)

    def register(self, head_dic):
        print('receve a register request')
        info_dic = {'username': head_dic['username'], 'passwd': head_dic['passwd'],
                    'homedir_size': settings.FILE_MAX_SIZE_LEVEL0, 'vip_level': 0}
        user_list = os.listdir(settings.DB_USER_DIR)
        if head_dic['username'] in user_list:
            res = struct.pack('i', 0)
            self.request.send(res)
            return
        res = struct.pack('i', 1)
        self.request.send(res)
        info_json = json.dumps(info_dic)
        user_reg_filepath = os.path.join(settings.DB_USER_DIR, head_dic['username'])
        user_homedir = os.path.join(settings.HOME_DIR, head_dic['username'])
        with open(user_reg_filepath, 'w') as f:
            f.write(info_json)
            os.mkdir(user_homedir)

    def login(self, head_dic):
        print('login')
        user_list = os.listdir(settings.DB_USER_DIR)
        if head_dic['username'] not in user_list:
            res = struct.pack('i', 0)   # 传输一个数字代表登录状态
            self.request.send(res)
            return
        user_filepath = os.path.join(settings.DB_USER_DIR, head_dic['username'])
        self.username = head_dic['username']
        self.current_dir = os.path.join(settings.HOME_DIR, self.username)
        with open(user_filepath, 'r') as f:
            file_head_dic = json.loads(f.read())
            self.homedir_size = file_head_dic['homedir_size']
            print(file_head_dic)
            if head_dic['username'] == file_head_dic['username'] and head_dic['passwd'] == file_head_dic['passwd']:
                res = struct.pack('i', 2)
                self.request.send(res)
                return
            else:
                res = struct.pack('i', 1)
                self.request.send(res)
                return

    def cd(self, head_dic):
        cmd = head_dic['cmd']
        # cmd_split = cmd.split()
        if len(head_dic) == 1:
            self.current_dir = os.path.join(settings.HOME_DIR, self.username)
        if len(head_dic) == 2:
            if head_dic['check_dir'] == '../':
                if len(self.current_dir) > len(os.path.join(settings.HOME_DIR, self.username)):
                    self.current_dir = os.path.dirname(self.current_dir)
                else:
                    print('没有上一级目录')
            else:
                if not os.path.exists(head_dic['check_dir']):
                    print('此目录不存在')
                self.current_dir = os.path.join(self.current_dir, head_dic['check_dir'])
        print('current dir is:', self.current_dir)

    def ls(self, head_dic):
        self.cmd(head_dic)

    def pwd(self, head_dic):
        self.cmd(head_dic)

    def dir(self, head_dic):
        self.cmd(head_dic)

    def cmd(self, head_dic):

        os.chdir(self.current_dir)
        res = subprocess.Popen(head_dic['cmd'], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        std_out = res.stdout.read()
        err_out = res.stderr.read()
        data_size = len(std_out) + len(err_out)
        print(data_size)
        # 报头byte化
        head_dic_send = {'data_size': data_size}
        head_json = json.dumps(head_dic_send)
        head_bytes = head_json.encode('utf-8')

        # 报头byte了，但是客户端并不知道报头的长度是多少，但是字典格式的报头用struct就是4bytes
        res = struct.pack('i', len(head_bytes))

        # 1. 发送报头长度，固定4bytes
        print(len(res), res)
        self.request.send(res)
        # 2. 发送报头内容
        self.request.send(head_bytes)
        # 3. 发送数据
        self.request.send(std_out)
        self.request.send(err_out)




def run():
    obj = socketserver.ThreadingTCPServer(settings.SERVER_ADDRESS, FTPSERVER)
    obj.serve_forever()     # 提供链接循环
    '''
    def finish_request(self, request, client_address):
    Finish one request by instantiating RequestHandlerClass.
    self.RequestHandlerClass(request, client_address, self)
    '''


