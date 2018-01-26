#!/usr/bin/env python
# _*_ coding:utf8 _*_

import socket
import struct
import json
import os



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


    def put(self,args):
        cmd=args[0]
        filename=args[1]
        if not os.path.isfile(filename):
            print('file:%s is not exists' %filename)
            return
        else:
            filesize=os.path.getsize(filename)

        head_dic={'cmd':cmd,'filename':os.path.basename(filename),'filesize':filesize}
        print(head_dic)
        head_json=json.dumps(head_dic)
        head_json_bytes=bytes(head_json,encoding=self.coding)

        head_struct=struct.pack('i',len(head_json_bytes))
        self.socket.send(head_struct)
        self.socket.send(head_json_bytes)
        send_size=0
        with open(filename,'rb') as f:
            for line in f:
                self.socket.send(line)
                send_size+=len(line)
                print(len(line), send_size)
            else:
                print('upload successful')

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
        while recv_size < data_size:
            recv_data = self.socket.recv(1024)
            f.write(recv_data)
            recv_size += len(recv_data)
            print(recv_size)
        f.close()
        print('download finish')

client=MYTCPClient(('127.0.0.1', 9004))
client.run()

# put D:\\GoogleDownload\\python-3.6.4.exe
# put D:\\GoogleDownload\\SourceTreeSetup_1.4.1.exe
# put D:\\GoogleDownload\\Python-3.6.4.tgz
# get python-3.6.4.exe
# get SourceTreeSetup_1.4.1.exe
