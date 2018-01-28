#!/usr/bin/env python
# _*_ coding:utf8 _*_

import hashlib
import socket
import struct
import json

class my_sock:
    address_family = socket.AF_INET
    socket_type = socket.SOCK_STREAM
    allow_reuse_address = False
    max_packet_size = 8192
    coding = 'utf-8'
    request_queue_size = 5

    def __init__(self, server_address, connect=True):
        self.server_address = server_address
        self.socket = socket.socket(self.address_family,
                                    self.socket_type)
        if connect:
            try:
                self.client_connect()
            except:
                self.client_close()
                raise

    def client_connect(self):
        self.socket.connect(self.server_address)

    def client_close(self):
        self.socket.close()




def dic_to_bytes(dic):
    dic_str = json.dumps(dic)
    dic_bytes = bytes(dic_str, encoding='utf-8')
    return dic_bytes

