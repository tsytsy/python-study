#!/usr/bin/env python
# _*_ coding:utf8 _*_

import socket
chat_dict = {'武大郎': ('127.0.0.1', 8001), '西门庆': ('127.0.0.1', 8002)}

# TO_ADDR = ('127.0.0.1', 8001)
udpsock_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    print('请选择聊天对象:', end='')
    people = input()
    if people not in chat_dict:
        print('您没有此好友')
        continue
    break

while True:
    print('请输入消息，回车发送:', end='')
    to = input().strip()
    if to == 'q':
        break
    udpsock_client.sendto(to.encode('utf-8'), chat_dict[people])
    feedback, server_addr = udpsock_client.recvfrom(1024)
    print('有一条来自[%s:%s]的消息:%s' % (server_addr[0], server_addr[1], feedback.decode('utf-8')))
udpsock_client.close()


