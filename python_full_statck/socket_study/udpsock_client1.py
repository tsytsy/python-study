#!/usr/bin/env python
# _*_ coding:utf8 _*_
import socket
TO_ADDR = ('127.0.0.1', 8000)
udpsock_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    to = input(">>:").strip()
    if to == 'q':
        break
    udpsock_client.sendto(to.encode('utf-8'), TO_ADDR)
    feedback, server_addr = udpsock_client.recvfrom(1024)
    print(feedback.decode('utf-8'))
    print(server_addr)
udpsock_client.close()

