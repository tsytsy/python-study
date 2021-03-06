# import socket
# s_cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s_cli.connect(('127.0.0.1', 8080))
# 'Send a data string to the socket.  For the optional flags'
# '''
# 当send一个空字符时，虽然客服端可以发送出去，但是服务端的receive没有收到字符
# '''
# while True:
#     char = input('>>:'.strip())
#     if not char:
#         continue
#     num = s_cli.send(char.encode('utf-8'))
#     print('num:', num)
#     data = s_cli.recv(1024)
#     print('data', data)
# s_cli.close()
import socket
phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
phone.connect(('127.0.0.1', 6000))
while True:   # 可以循环接收发送消息
    char = input('>>').strip()
    if not char:  # 防止发送空字符
        continue
    phone.send(char.encode('utf-8'))
    data = phone.recv(1024)
    print(data.decode('utf-8'))
phone.close()