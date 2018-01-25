#!/usr/bin/env python
# _*_ coding:utf8 _*_
import socketserver
import subprocess
import json
import struct
'''
To implement a service, you must derive a class from
BaseRequestHandler and redefine its handle() method.  You can then run
various versions of the service by combining one of the server classes
with your request handler class.
'''
class FTPSERVER(socketserver.BaseRequestHandler):
    def handle(self):
        print(self.request)  # connect连上了
        print(self.client_address)
        # print(self.server)
        while True:  # 通信循环
            try:
                rec_data = self.request.recv(1024).decode("utf-8")
                if not rec_data:
                    break
                print(rec_data)
                res = subprocess.Popen(rec_data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                std_out = res.stdout.read()
                err_out = res.stderr.read()
                data_size = len(std_out) + len(err_out)
                print(data_size)
                # 报头byte化
                head_dic = {'data_size': data_size}
                head_json = json.dumps(head_dic)
                head_bytes = head_json.encode('utf-8')

                # 报头byte了，但是客户端并不知道报头的长度是多少，但是字典格式的报头用struct就是4bytes
                res = struct.pack('i', len(head_bytes))

                # 1. 发送报头长度，固定4bytes
                self.request.send(res)
                # 2. 发送报头内容
                self.request.send(head_bytes)
                # 3. 发送数据
                self.request.send(std_out)
                self.request.send(err_out)

            except Exception as e:
                print(e)
                break
if __name__ == '__main__':
    obj = socketserver.ThreadingTCPServer(('127.0.0.1', 8001), FTPSERVER)
    obj.serve_forever()  # 连接循环解决
    """
    Handle one request at a time until shutdown.
    Polls for shutdown every poll_interval seconds. Ignores
    self.timeout. If you need to do periodic tasks, do them in
    another thread.
    """


