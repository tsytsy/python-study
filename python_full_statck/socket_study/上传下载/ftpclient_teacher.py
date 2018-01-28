#!/usr/bin/env python
# _*_ coding:utf8 _*_

import socket
import struct
import json
import os
import hashlib


class MYTCPClient:
    address_family = socket.AF_INET

    socket_type = socket.SOCK_STREAM

    allow_reuse_address = False

    max_packet_size = 8192

    coding='utf-8'

    request_queue_size = 5

    def __init__(self, server_address, connect=True):
        self.server_address=server_address
        self.socket = socket.socket(self.address_family,
                                    self.socket_type)
        if connect:
            try:
                self.client_connect()
            except:
                self.client_close()
                raise

    def client_connect(self):
        self.socket.connect(self.server_address)

    def client_close(self):
        self.socket.close()

    def run(self):
        while True:
            inp=input(">>: ").strip()
            if not inp:continue
            l=inp.split()
            cmd=l[0]
            if hasattr(self,cmd):
                func=getattr(self,cmd)
                func(l)
            else:
                print('不存在这个命令，请重新输入')


    def put(self, args):
        cmd = args[0]
        filename = args[1]
        if not os.path.isfile(filename):
            print('file:%s is not exists' % filename)
            return
        else:
            filesize = os.path.getsize(filename)
        head_dic = {'cmd': cmd, 'filename': os.path.basename(filename), 'filesize': filesize}
        print(head_dic)
        head_json = json.dumps(head_dic)
        head_json_bytes=bytes(head_json, encoding=self.coding)

        head_struct = struct.pack('i', len(head_json_bytes))
        self.socket.send(head_struct)
        self.socket.send(head_json_bytes)
        send_size = 0

        with open(filename,'rb') as f:
            my_md5 = hashlib.md5()
            for line in f:
                self.socket.send(line)
                my_md5.update(line)
                send_size += len(line)
                self.process(send_size, filesize)
            else:
                print('upload successful')
                my_md5_str = my_md5.hexdigest()
                print('send file md5 is:', my_md5_str)
                my_md5_bytes = bytes(my_md5_str, encoding='utf-8')
                self.socket.send(my_md5_bytes)

    def get(self, args):
        cmd = args[0]
        filename = args[1]
        RECV_BASE_DIR = os.path.join(r'D:\GoogleDownload', 'file_download')

        head_dic = {'cmd': cmd, 'filename': os.path.basename(filename)}
        # print(head_dic)
        head_json = json.dumps(head_dic)
        head_json_bytes = bytes(head_json, encoding=self.coding)

        head_struct = struct.pack('i', len(head_json_bytes))
        self.socket.send(head_struct)
        self.socket.send(head_json_bytes)

        head_recv_len = self.socket.recv(4)[0]
        if not head_recv_len:
            print('服务端不存在这个文件')
            return
        head_recv_bytes = self.socket.recv(head_recv_len)
        head_recv_json = head_recv_bytes.decode('utf-8')
        head_recv_dic =json.loads(head_recv_json)
        data_size = head_recv_dic['datasize']
        file_recv_name = head_recv_dic['filename']
        file_path = os.path.join(RECV_BASE_DIR, file_recv_name)
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

client=MYTCPClient(('127.0.0.1', 9004))
client.run()

# put D:\\GoogleDownload\\python-3.6.4.exe
# put D:\\GoogleDownload\\SourceTreeSetup_1.4.1.exe
# put D:\\GoogleDownload\\Python-3.6.4.tgz
# put D:\\GoogleDownload\\BaiduNetdisk_5.7.2.3.exe
# put D:\\GoogleDownload\\Wireshark-win32-2.4.3.0.exe
# get python-3.6.4.exe
# get SourceTreeSetup_1.4.1.exe
# get BaiduNetdisk_5.7.2.3.exe


