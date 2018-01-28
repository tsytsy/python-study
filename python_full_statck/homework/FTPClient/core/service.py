#!/usr/bin/env python
# _*_ coding:utf8 _*_


import socket
import struct
import json
import os
import hashlib
from conf import common
from conf import settings

class Service(common.my_sock):
    def __init__(self, server_address, username):
        super(Service, self).__init__(server_address)
        self.username = username
        print('^^^^^^', username)
    def run(self):
        menu = '''
        1. 上传文件到服务器
        2. 从服务器端下载文件
        3. 对服务器目录进行操作
        q. 退出服务
        '''
        menu_dic = {
            '1': self.put,
            '2': self.get,
            '3': self.cmd,
            'q': exit
        }
        while True:
            print(menu)
            choose = input("请选择服务(编号)>>: ").strip()
            if not choose:
                continue
            if choose not in menu_dic:
                print('没有此服务，请重新选择')
                continue
            menu_dic[choose]()

    def put(self):
        filename = input('请输入上传文件路径:')
        cmd = 'put'
        if not os.path.isfile(filename):
            print('file:%s is not exists' % filename)
            return
        else:
            filesize = os.path.getsize(filename)
        head_dic = {'cmd': cmd, 'filename': os.path.basename(filename), 'filesize': filesize, 'username': self.username}
        print(head_dic)
        head_json = json.dumps(head_dic)
        head_json_bytes = bytes(head_json, encoding=self.coding)

        head_struct = struct.pack('i', len(head_json_bytes))
        self.socket.send(head_struct)
        self.socket.send(head_json_bytes)
        send_size = 0
        with open(filename, 'rb') as f:
            my_md5 = hashlib.md5()
            for line in f:
                self.socket.send(line)
                my_md5.update(line)
                send_size += len(line)
                self.process(send_size, filesize)   # 打印进度条
            else:
                print('upload successful')
                my_md5_str = my_md5.hexdigest()     # 传输一致性
                print('send file md5 is:', my_md5_str)
                my_md5_bytes = bytes(my_md5_str, encoding='utf-8')
                self.socket.send(my_md5_bytes)

    def get(self):
        cmd = 'get'
        filename = input('下载的文件名为:')

        head_dic = {'cmd': cmd, 'filename': os.path.basename(filename), 'username': self.username}
        head_json = json.dumps(head_dic)
        head_json_bytes = bytes(head_json, encoding=self.coding)
        head_struct = struct.pack('i', len(head_json_bytes))
        self.socket.send(head_struct)
        self.socket.send(head_json_bytes)
        print('send head over')
        head_recv_len = self.socket.recv(4)[0]
        if not head_recv_len:
            print('服务端不存在这个文件')
            return
        head_recv_bytes = self.socket.recv(head_recv_len)
        head_recv_json = head_recv_bytes.decode('utf-8')
        head_recv_dic =json.loads(head_recv_json)
        data_size = head_recv_dic['datasize']
        file_recv_name = head_recv_dic['filename']
        file_recv_path = os.path.join(settings.RECV_BASE_DIR, self.username)
        if not os.path.exists(file_recv_path):
            os.makedirs(file_recv_path)
        file_path = os.path.join(file_recv_path, file_recv_name)
        recv_size = 0
        f = open(file_path, 'wb')
        recv_md5_obj = hashlib.md5()
        while recv_size < data_size:
            minus = data_size - recv_size
            if minus > 1024:
                size = 1024
            else:
                size = minus
            recv_data = self.socket.recv(size)

            f.write(recv_data)
            recv_md5_obj.update(recv_data)
            recv_size += len(recv_data)
            self.process(recv_size, data_size)
        f.close()
        print('download finish')
        recv_md5_str = recv_md5_obj.hexdigest()
        print(recv_md5_str)
        send_md5_bytes = self.socket.recv(32)
        send_md5_str = send_md5_bytes.decode('utf-8')
        print('收到：', send_md5_str)
        if send_md5_str == recv_md5_str:
            print('下载的文件与源文件一致')
        else:
            print('下载的文件与源文件不一致，删除请重新下载')
            os.remove(file_path)

    def process(self, size, total_size):
        percent = size / total_size
        percent1 = round(percent * 100, 2)
        NUM_OF_STAR = int(percent * 100 / 2)
        print('[%s]%s%%' % ('#' * NUM_OF_STAR, percent1))

    def cmd(self):
        while True:
            command = input("输入命令(按b返回上一级)>>:").strip()
            if not command:
                continue
            if command == 'b':
                break
            cmd = 'cmd'  # 对应服务端

            head_dic = {'cmd': cmd, 'command': command, 'username': self.username}
            head_json = json.dumps(head_dic)
            head_json_bytes = bytes(head_json, encoding=self.coding)
            head_struct = struct.pack('i', len(head_json_bytes))
            print('^&^&^&^&^&', len(head_struct))
            self.socket.send(head_struct)
            self.socket.send(head_json_bytes)
            # self.socket.send(command.encode('utf-8'))
            # # 1. 获得报头的长度
            head_len = struct.unpack('i', self.socket.recv(4))[0]
            # print('head length', head_len)
            # # 2. 获取报头字典
            head_bytes = self.socket.recv(head_len)
            head_json = head_bytes.decode('utf-8')
            head_dic = json.loads(head_json)
            # print('head_dic', head_dic)
            # # 3. 从报头字典中获取数据长度
            data_size = head_dic['data_size']
            print('data size:', data_size)
            recv_size = 0
            recv_data = b''
            while recv_size < data_size:
                data = self.socket.recv(1024)
                recv_size += len(data)
                recv_data += data
            #
            # print(len(recv_data))
            print(recv_data.decode("gbk"))




# client=MYTCPClient(('127.0.0.1', 9004))
# client.run()

# put D:\\GoogleDownload\\python-3.6.4.exe
# put D:\\GoogleDownload\\SourceTreeSetup_1.4.1.exe
# put D:\\GoogleDownload\\Python-3.6.4.tgz
# put D:\\GoogleDownload\\BaiduNetdisk_5.7.2.3.exe
# put D:\\GoogleDownload\\Wireshark-win32-2.4.3.0.exe
# get python-3.6.4.exe
# get SourceTreeSetup_1.4.1.exe
# get BaiduNetdisk_5.7.2.3.exe