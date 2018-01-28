#!/usr/bin/env python
# _*_ coding:utf8 _*_
import time
import socket
import socketserver
import struct
import json
import os
import logging
import hashlib

def Mylogger():
    logger = logging.getLogger()
    fm = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
    file_path = os.path.join('file_load', 'receive.txt')
    # print(file_path)
    fh = logging.FileHandler(file_path)
    sh = logging.StreamHandler()
    fh.setFormatter(fm)
    sh.setFormatter(fm)
    logger.addHandler(fh)
    logger.addHandler(sh)
    logger.setLevel(10)
    return logger

class FTPSERVER(socketserver.BaseRequestHandler):
    def handle(self):
        print(self.client_address, 'connected')
        while True:
            head_len = struct.unpack('i', self.request.recv(4))[0]
            head_bytes = self.request.recv(head_len)
            head_json = head_bytes.decode('utf-8')
            head_dict = json.loads(head_json)
            print(head_dict)
            cmd = head_dict['cmd']
            if hasattr(self, cmd):
                func = getattr(self, cmd)
                func(head_dict)
            else:
                break

    def put(self, head_dict):
        # logger = Mylogger()
        recv_md5_file = hashlib.md5()
        BASE_DIR = os.path.join(os.getcwd(), 'file_upload')
        file_name = os.path.join(BASE_DIR, head_dict['filename'])
        if not os.path.exists(BASE_DIR):
            os.mkdir(BASE_DIR)
        file_size = head_dict['filesize']
        f = open(file_name, 'wb')
        recv_size = 0
        time.sleep(10)
        while recv_size < file_size:
            minus = file_size - recv_size
            if minus > 1024:
                size = 1024
            else:
                size = minus
            data = self.request.recv(size)
            f.write(data)
            recv_md5_file.update(data)
            recv_size += len(data)
            # log = 'from {} the size is {}'.format(self.client_address, recv_size)
            # print(log)
            # logger.debug(log)
        print('put finish')
        recv_md5 = recv_md5_file.hexdigest()
        send_md5 = self.request.recv(32)
        print('recv md5 is:', recv_md5)
        if recv_md5 == send_md5.decode('utf-8'):
            print('收到的文件与接收的文件一致')
        else:
            print('收到的文件与源文件不一致，删除请重传')
            os.remove(file_name)
        f.close()

    def get(self, head):
        file_name = head['filename']
        if not os.path.exists(file_name):
            print(file_name)
            res = struct.pack('i', 0)
            self.request.send(res)
            return
        data_size = os.path.getsize(file_name)
        head_dic = {'filename': file_name, 'datasize': data_size}
        head_json = json.dumps(head_dic)
        head_bytes = head_json.encode('utf-8')
        res = struct.pack('i', len(head_bytes))

        self.request.send(res)
        self.request.send(head_bytes)
        f = open(file_name, 'rb')
        send_bytes = 0
        send_md5_obj = hashlib.md5()
        for line in f:
            self.request.send(line)
            send_md5_obj.update(line)
            send_bytes += len(line)
            print(send_bytes)
        f.close()
        print('send finish')
        send_md5_str = send_md5_obj.hexdigest()
        print('发送：', send_md5_str)
        send_md5_bytes = bytes(send_md5_str, encoding='utf-8')
        self.request.send(send_md5_bytes)




if __name__ == '__main__':
    IP_PORT = ('127.0.0.1', 9004)
    obj = socketserver.ThreadingTCPServer(IP_PORT, FTPSERVER)
    obj.serve_forever()     # 提供链接循环
    '''
        def finish_request(self, request, client_address):
        Finish one request by instantiating RequestHandlerClass.
        self.RequestHandlerClass(request, client_address, self)
    '''
