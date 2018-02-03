#!/usr/bin/env python
# _*_ coding:utf8 _*_

import socket
import select

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 9000))
server.listen(5)
inputs = [server, ]
while True:
    r, w, x = select.select(inputs, [], [])
    print(r)
    for i in r:
        if i == server:
            conn, addr = i.accept()
            inputs.append(conn)
        else:
            try:
                data = i.recv(1024)
                print(data.decode('utf8'))
                data1 = input('>>:')
                i.send(data1.encode('utf8'))
            except:
                inputs.remove(i)