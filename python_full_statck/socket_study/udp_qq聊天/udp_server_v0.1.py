#!/usr/bin/env python
# _*_ coding:utf8 _*_

import socket
IP_PORT = ("127.0.0.1", 8001)
udpsock_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udpsock_server.bind(IP_PORT)
# udpsock_server.listen(5)
print('start....')
while True:
    data, cli_addr = udpsock_server.recvfrom(1024)
    print('你有来自[%s:%s]的消息:%s' % (cli_addr[0], cli_addr[1], data.decode('utf-8')))
    print('回复消息:', end='')
    back = input().strip()
    udpsock_server.sendto(back.encode('utf-8'), cli_addr)
udpsock_server.close()

