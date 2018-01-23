import socket
phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
phone.connect(('127.0.0.1', 6000))
while True:   # 可以循环接收发送消息
    char = input('>>').strip()
    if not char:  # 防止发送空字符
        continue
    phone.send(char.encode('utf-8'))
    data = phone.recv(1024)
    print(data)
phone.close()