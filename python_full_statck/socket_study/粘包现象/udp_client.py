#!/usr/bin/env python
# _*_ coding:utf8 _*_

import socket
IP_PORT = ('127.0.0.1', 8082)
BUFFSIZE = 1024
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# while True:
client.sendto('hello.world'.encode('utf-8'), IP_PORT)
client.sendto('SB'.encode('utf-8'), IP_PORT)

