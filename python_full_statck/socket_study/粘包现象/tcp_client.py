#!/usr/bin/env python
# _*_ coding:utf8 _*_

import socket
IP_PORT = ('192.168.1.66', 9000)
BUFFSIZE = 1024
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(IP_PORT)

while True:
    command = input(">>input command:").strip()
    if not command:
        continue
    client.send(command.encode('utf-8'))
    recv1 = client.recv(4)
    while True:
        recv_data = client.recv(1024)
        print(len(recv_data))
        print(recv_data.decode('utf-8'))
