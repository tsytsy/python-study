import subprocess
import socket
ssh_cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ssh_cli.connect(("127.0.0.1", 9000))
command = input(">>input command:").strip()
ssh_cli.send(command.encode('utf-8'))
data = ssh_cli.recv(30000)
print(len(data), data.decode("gbk"))

# res = subprocess.Popen("ls", shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
# data = res.stderr.read()
# print(data.decode('gbk').encode('utf-8').decode('utf-8'))
