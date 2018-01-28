#!/usr/bin/env python
# _*_ coding:utf8 _*_

import json
import struct
import socket
# def data_pack(data):
#     data_bytes = data.encode('utf-8')
#     data_len = len(data_bytes)
#     head_dic = {'filesize': data_len}
#     head_dic_json = json.dumps(head_dic)
#     head_dic_bytes = head_dic_json.encode('utf-8')
#     head_struct = struct.pack('i', len(head_dic_bytes))
#     return head_struct, head_dic_bytes, data_bytes

#
# def send(*args,**kwargs):
#     socket.socket.send()
