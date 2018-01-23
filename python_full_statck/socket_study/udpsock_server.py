#!/usr/bin/env python
# _*_ coding:utf8 _*_
import socket
IP_PORT = ("127.0.0.1", 8000)
udpsock_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# a2, a1 = udpsock_server.getsockname()
udpsock_server.bind(IP_PORT)
# udpsock_server.listen(5)
print('start....')
while True:
    data, cli_addr = udpsock_server.recvfrom(1024)
    print('data-->', data)
    print('cli_addr-->', cli_addr)
    udpsock_server.sendto(data.upper(), cli_addr)
udpsock_server.close()

