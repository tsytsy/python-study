import socket
import subprocess

ssh_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ssh_server.bind(("127.0.0.1", 9000))
while True:
    ssh_server.listen(5)
    conn, addr = ssh_server.accept()
    while True:  # 循环数据交互
        try:
            rec_data = conn.recv(1024).decode("utf-8")
            print(rec_data)

            res = subprocess.Popen(rec_data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            err = res.stderr.read()
            if err:
                print(type(err), err.decode('gbk'))
                conn.send(err)
            else:
                conn.send(res.stdout.read())
        except Exception as e:
            print(e)
            break
    conn.close()
ssh_server.close()
# print(data.decode("gbk"))