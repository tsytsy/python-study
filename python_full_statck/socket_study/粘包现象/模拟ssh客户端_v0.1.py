import subprocess
import socket
import struct
ssh_cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ssh_cli.connect(("192.168.1.66", 9000))
while True:
    command = input(">>input command:").strip()
    if not command:
        continue
    ssh_cli.send(command.encode('utf-8'))
    data_size = struct.unpack('i', ssh_cli.recv(4))[0]
    print('data size:', data_size)
    recv_size = 0
    recv_data = b''
    while recv_size < data_size:
        data = ssh_cli.recv(1024)
        recv_size += len(data)
        recv_data += data

    print(len(recv_data))
    print(recv_data.decode("utf-8"))
    if command == 'q':
        break
ssh_cli.close()

# res = subprocess.Popen("ls", shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
# data = res.stderr.read()
# print(data.decode('gbk').encode('utf-8').decode('utf-8'))
