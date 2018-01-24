#!/usr/bin/env python
# _*_ coding:utf8 _*_

import socket
IP_PORT = ('127.0.0.1', 8082)
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(IP_PORT)


# while True:
data1, addr1 = server.recvfrom(1024)
data2, addr2 = server.recvfrom(1024)
print(data1.decode('utf-8'))
print(data2.decode('utf-8'))

