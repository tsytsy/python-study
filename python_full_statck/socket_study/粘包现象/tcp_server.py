#!/usr/bin/env python
# _*_ coding:utf8 _*_
import socket
IP_PORT = ('127.0.0.1', 8080)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(IP_PORT)
server.listen(5)
conn, client_addr = server.accept()
# while True:
data1 = conn.recv(1024)
data2 = conn.recv(1024)
print(data1.decode('utf-8'))
print(data2.decode('utf-8'))
conn.close()

