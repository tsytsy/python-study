import subprocess
import socket
ssh_cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ssh_cli.connect(("192.168.1.66", 9000))
while True:
    command = input(">>input command:").strip()
    if not command:
        continue
    ssh_cli.send(command.encode('utf-8'))
    data = ssh_cli.recv(30000)
    print(len(data), data.decode("utf-8"))
    if command == 'q':
        break
ssh_cli.close()

# res = subprocess.Popen("ls", shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
# data = res.stderr.read()
# print(data.decode('gbk').encode('utf-8').decode('utf-8'))
