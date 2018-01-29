#!/usr/bin/env python
# _*_ coding:utf8 _*_

import hashlib
import socket
import struct
import json

class my_sock:
    address_family = socket.AF_INET
    socket_type = socket.SOCK_STREAM
    allow_reuse_address = False
    max_packet_size = 8192
    coding = 'utf-8'
    request_queue_size = 5

    def __init__(self, server_address, connect=True):
        self.server_address = server_address
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

    def pack_send(self, dic):
        dic_bytes = dic_to_bytes(dic)
        head_struct = struct.pack('i', len(dic_bytes))  # 4bytes数据表示reg_dic的长度，如80
        self.socket.send(head_struct)
        self.socket.send(dic_bytes)

    def receive_unpack(self, length):
        head_recv_bytes = self.socket.recv(length)
        head_recv_json = head_recv_bytes.decode('utf-8')
        head_recv_dic = json.loads(head_recv_json)
        return head_recv_dic

    def ssh_client(self, args):
        cmd = ' '.join(args)
        head_dic = {'cmd': cmd}
        self.pack_send(head_dic)
        head_len = struct.unpack('i', self.socket.recv(4))[0]
        head_dic = self.receive_unpack(head_len)
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


def dic_to_bytes(dic):
    dic_str = json.dumps(dic)
    dic_bytes = bytes(dic_str, encoding='utf-8')
    return dic_bytes

