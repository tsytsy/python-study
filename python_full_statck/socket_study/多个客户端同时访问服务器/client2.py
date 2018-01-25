#!/usr/bin/env python
# _*_ coding:utf8 _*_

import subprocess
import socket
import struct
import json
ssh_cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ssh_cli.connect(("127.0.0.1", 8001))
# ssh_cli.connect(("192.168.1.66", 9001))
while True:
    command = input(">>input command:").strip()
    if not command:
        continue
    if command == 'q':
        break
    ssh_cli.send(command.encode('utf-8'))
    # 1. 获得报头的长度
    head_len = struct.unpack('i', ssh_cli.recv(4))[0]
    print('head length', head_len)
    # 2. 获取报头字典
    head_bytes = ssh_cli.recv(head_len)
    head_json = head_bytes.decode('utf-8')
    head_dic = json.loads(head_json)
    print('head_dic', head_dic)
    # 3. 从报头字典中获取数据长度
    data_size = head_dic['data_size']
    print('data size:', data_size)
    recv_size = 0
    recv_data = b''
    while recv_size < data_size:
        data = ssh_cli.recv(1024)
        recv_size += len(data)
        recv_data += data

    print(len(recv_data))
    # print(recv_data.decode("utf-8"))
    print(recv_data.decode("gbk"))
ssh_cli.close()

