#!/usr/bin/env python
# _*_ coding:utf8 _*_
'''

IO多路复用的机制有三种:select,poll,epoll
select缺点
1. 每次调用select都要将所有的fd拷贝到内核空间。导致效率降低。
2. 遍历所有的fd是否有数据访问。每一次监听都需要遍历。循环遍历(最大的缺点)
3. 最大连接数1024

poll
相对于select，没有最大的连接数限制，其他的都一样。

epoll
1. 创建句柄:将所有的fd拷贝到内核空间，但只需要拷贝一次
2. 回调函数:某一个动作成功完成之后会触发的函数，为所有的fd绑定一个回调函数。
    一旦有数据访问，触发该回调函数，将fd放到一个列表

打个比喻
将一个班的学生交试卷比作多路复用。
select版本
老师要到教室下面去一个个问，你要交卷吗？如果需要交卷，将卷子放到一个列表里，继续问下一个同学，你需要交卷吗？
以此往复。问完一遍之后，又重新开始从第一个同学开始问，你需要交卷吗?.......
epoll版本
给每个同学安装一个按铃(回调函数)，如果某个同学想交卷，那么直接按铃，老师去收卷子就好了
'''

import socket
import selectors


def accept(sock, mask):
    conn, addr = sock.accept()
    sel.register(conn, selectors.EVENT_READ, read)


def read(conn, mask):
    try:
        recv_data = conn.recv(1024)
        print(recv_data.decode('utf8'))
        data = input('>>:')
        conn.send(data.encode('utf8'))
    except:
        sel.unregister(conn)


if __name__ == '__main__':

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 9000))
    server.listen(5)
    sel = selectors.DefaultSelector()     # g根据具体平台选择IO多路复用的机制(select, poll, epoll)

    sel.register(server, selectors.EVENT_READ, accept)
    while True:
        events = sel.select()
        print(events)
        for key, mask in events:
            callback = key.data
            callback(key.fileobj, mask)
