import socket
s1 = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
# print(type(s1))
s1.bind(('127.0.0.1', 8080))
s1.listen(5)

'''
Wait for an incoming connection.  Return a new socket
representing the connection, and the address of the client.
For IP sockets, the address info is a pair (hostaddr, port)
'''

while True:
    print('start.....')
    s_fromcli, addr = s1.accept()
    print(s_fromcli)
    print('client addr:', addr)
    'receive up to buffersize bytes from the socket.'
    while True:
        try:
            data = s_fromcli.recv(1024)
            print('data', data)
            'Send a data string to the socket'
            s_fromcli.send(data.upper())
        except Exception:
            break
    s_fromcli.close()




