#!/usr/bin/env python
# _*_ coding:utf8 _*_

import socket
import struct
import json

class FTPSEVER:
    address_family = socket.AF_INET
    sock_type = socket.SOCK_STREAM
    request_queue_size = 5
    allow_reuse_address = True
    bind_and_activate = True

    def __init__(self, address):
        self.sock = socket.socket(self.address_family, self.sock_type)
        self.address = address
        if self.bind_and_activate:
            self.bind(self.address)
            self.active()
        else:
            self.close()

    def bind(self, address):
        self.sock.bind(address)

    def active(self):
        self.sock.listen(self.request_queue_size)

    def run(self):
        while True:
            conn, addr = self.sock.accept()
            self.conn = conn
            while True:
                head_len = struct.unpack('i', conn.recv(4))[0]
                head_bytes = conn.recv(head_len)
                head_json = head_bytes.decode('utf-8')
                head_dict = json.loads(head_json)
                print(head_dict)
                cmd = head_dict['cmd']
                if hasattr(self, cmd):
                    func = getattr(self, cmd)
                    func(head_dict)
                else:
                    break

    def put(self, head_dict1):
            file_name = head_dict1['filename']
            file_size = head_dict1['filesize']
            f = open(file_name, 'wb')
            recv_size = 0
            while recv_size < file_size:
                data = self.conn.recv(1024)
                f.write(data)
                recv_size += len(data)
            f.close()

    def get(self):
        pass
    def close(self):
        pass


ftp_server = FTPSEVER(('127.0.0.1', 9004))
ftp_server.run()


