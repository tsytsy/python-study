# import socket
# s1 = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
# # print(type(s1))
# s1.bind(('127.0.0.1', 8080))
# s1.listen(5)
#
# '''
# Wait for an incoming connection.  Return a new socket
# representing the connection, and the address of the client.
# For IP sockets, the address info is a pair (hostaddr, port)
# '''
#
# while True:
#     print('start.....')
#     s_fromcli, addr = s1.accept()
#     print(s_fromcli)
#     print('client addr:', addr)
#     'receive up to buffersize bytes from the socket.'
#     while True:
#         try:
#             data = s_fromcli.recv(1024)
#             print('data', data)
#             'Send a data string to the socket'
#             s_fromcli.send(data.upper())
#         except Exception:
#             break
#     s_fromcli.close()

import socket
phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
phone.bind(('127.0.0.1', 6000))
while True:  # 服务端不掉线
    phone.listen(5)  # ?5
    print('start...')
    conn, addr = phone.accept()
    print(conn)
    print(addr)
    while True:  # 可以循环发送接收消息
        try:
            data = conn.recv(1024)  # ?1024
            print(data.decode('utf-8'))
            conn.send(data.upper())
        except Exception as e:
            print(e)
            break
    # conn.send('hello'.encode('utf-8'))
    conn.close()
phone.close()

