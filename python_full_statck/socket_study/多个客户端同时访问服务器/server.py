#!/usr/bin/env python
# _*_ coding:utf8 _*_

import socket
import subprocess
import struct
import json
ssh_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ssh_server.bind(("127.0.0.1", 9001))
ssh_server.listen(5)
while True:   # 链接循环
    conn, addr = ssh_server.accept()
    print('建立连接....')
    while True:  # 通信循环
        try:
            rec_data = conn.recv(1024).decode("utf-8")
            if not rec_data:
                break
            print(rec_data)
            res = subprocess.Popen(rec_data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            std_out = res.stdout.read()
            err_out = res.stderr.read()
            data_size = len(std_out) + len(err_out)
            print(data_size)
            # 报头byte化
            head_dic = {'data_size': data_size}
            head_json = json.dumps(head_dic)
            head_bytes = head_json.encode('utf-8')

            # 报头byte了，但是客户端并不知道报头的长度是多少，但是字典格式的报头用struct就是4bytes
            res = struct.pack('i', len(head_bytes))

            # 1. 发送报头长度，固定4bytes
            conn.send(res)
            # 2. 发送报头内容
            conn.send(head_bytes)
            # 3. 发送数据
            conn.send(std_out)
            conn.send(err_out)

        except Exception as e:
            print(e)
            break
    conn.close()
ssh_server.close()