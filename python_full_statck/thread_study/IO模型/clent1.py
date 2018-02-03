#!/usr/bin/env python
# _*_ coding:utf8 _*_



import socket
sk=socket.socket()
sk.connect(('127.0.0.1',9000))

while True:
    inp=input(">>>>")   # how much one night?
    sk.sendall(bytes(inp,"utf8"))
    data=sk.recv(1024)
    print(str(data,'utf8'))