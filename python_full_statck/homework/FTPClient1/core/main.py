#!/usr/bin/env python
# _*_ coding:utf8 _*_
from conf import common
from core import ftp_client
from conf import settings
import socket
import struct
import hashlib
import json
import os


class start(ftp_client.MyFtpClient):
    def __init__(self, server_address):
    #     self.server_address = server_address
        common.my_sock.__init__(self, server_address)
        self.begin()
    def begin(self):
        menu = '''
        1. 注册
        2. 登录
        q. 退出
        '''
        menu_dic = {
            '1': self.register,
            '2': self.login,
            'q': self.quit_menu
        }
        while True:
            print(menu)
            choose = input('>>:')
            if choose in menu_dic:
                menu_dic[choose]()
            else:
                print('输入错误，请重新选择服务')

    def register(self):     # 可以在此函数中进行拓展
        print('register')
        username = input('注册用户名>>:')
        passwd = input('注册用户密码>>:')
        super(start, self).register(username, passwd)
        self.reg_recvfrom_server()

    def login(self):    # 可以在此函数中进行拓展
        username = input('username>>:')
        passwd = input('passwd>>:')
        print('#######')
        super(start, self).login(username, passwd)
        num = self.login_recvfrom_server()
        if num == 2:
            self.run()
# ------------------------------二级菜单分割线-----------------------------------------#

    def run(self):
        menu = '''
        1. 上传文件到服务器(put)
        2. 从服务器端下载文件(get)
        3. 改变文件路径(cd)
        4. 查看文件目录(ls,dir)
        5. 查看当前路径(pwd)
        6. 冲会员
        q. 退出服务
        '''
        menu_dic = {
            '1': self.put,
            '2': self.get,
            '3': self.cd,
            '4': self.ls,
            '5': self.pwd,
            '6': self.charge,
            'q': exit
        }
        while True:
            print(menu)
            # choose = input("请选择服务(编号)>>: ").strip()
            # if not choose:
            #     continue
            # if choose not in menu_dic:
            #     print('没有此服务，请重新选择')
            #     continue
            #
            # menu_dic[choose]()
            cmd_str = input('输入相关命令>>:')
            if cmd_str == 'q':
                exit()
            cmd_list = cmd_str.split()
            if hasattr(self, cmd_list[0]):
                func = getattr(self, cmd_list[0])
            else:
                print('命令错误，请重新输入')
                continue
            func(cmd_list)

    def put(self, args):
        if len(args) == 1:
            print('缺少参数，请重新输入')
            return
        filename = args[1]
        cmd = args[0]
        if not os.path.isfile(filename):
            print('file:%s is not exists' % filename)
            return
        else:
            filesize = os.path.getsize(filename)
        head_dic = {'cmd': cmd, 'filename': os.path.basename(filename), 'filesize': filesize}
        self.pack_send(head_dic)
        print('read to recv')
        space_isenough = self.socket.recv(4)[0]
        print('space_isenough:', space_isenough)
        if not space_isenough:
            print('磁盘空间不足')
            return
        send_size = 0
        print('continue')
        with open(filename, 'rb') as f:
            my_md5 = hashlib.md5()
            for line in f:
                self.socket.send(line)
                my_md5.update(line)
                send_size += len(line)
                self.process(send_size, filesize)   # 打印进度条
            else:
                print('upload successful')
                my_md5_str = my_md5.hexdigest()     # 传输一致性
                print('send file md5 is:', my_md5_str)
                my_md5_bytes = bytes(my_md5_str, encoding='utf-8')
                self.socket.send(my_md5_bytes)
        issame_byte = self.socket.recv(4)
        print(issame_byte)
        issame = struct.unpack('i', issame_byte)
        if issame:
            print('文件传输一致')
        else:
            print('文件传输出现错误，请重新上传')
    def get(self, args):
        if len(args) == 1:
            print('缺少参数，请重新输入')
            return
        filename = args[1]
        cmd = args[0]
        head_dic = {'cmd': cmd, 'filename': os.path.basename(filename)}
        self.pack_send(head_dic)
        print('send head over')
        head_recv_len = self.socket.recv(4)[0]
        if not head_recv_len:
            print('服务端不存在这个文件')
            return
        head_recv_dic = self.receive_unpack(head_recv_len)
        data_size = head_recv_dic['datasize']
        file_recv_name = head_recv_dic['filename']
        file_recv_path = os.path.join(settings.RECV_BASE_DIR)
        if not os.path.exists(file_recv_path):
            os.makedirs(file_recv_path)
        file_path = os.path.join(file_recv_path, file_recv_name)
        recv_size = 0
        f = open(file_path, 'wb')
        recv_md5_obj = hashlib.md5()
        while recv_size < data_size:
            minus = data_size - recv_size
            if minus > 1024:
                size = 1024
            else:
                size = minus
            recv_data = self.socket.recv(size)
            f.write(recv_data)
            recv_md5_obj.update(recv_data)
            recv_size += len(recv_data)
            self.process(recv_size, data_size)
        f.close()
        print('download finish')
        recv_md5_str = recv_md5_obj.hexdigest()
        print(recv_md5_str)
        send_md5_bytes = self.socket.recv(32)
        send_md5_str = send_md5_bytes.decode('utf-8')
        print('收到：', send_md5_str)
        if send_md5_str == recv_md5_str:
            print('下载的文件与源文件一致')
        else:
            print('下载的文件与源文件不一致，删除请重新下载')
            os.remove(file_path)

    def quit_menu(self, args):
        exit()

    def process(self, size, total_size):
        percent = size / total_size
        percent1 = round(percent * 100, 2)
        NUM_OF_STAR = int(percent * 100 / 2)
        print('[%s]%s%%' % ('#' * NUM_OF_STAR, percent1))

    def cd(self, args):
        if len(args) == 1:
            cmd_dic = {'cmd': 'cd'}
        if len(args) == 2:
            cmd_dic = {'cmd': 'cd', 'check_dir': args[-1]}
        self.pack_send(cmd_dic)

    def ls(self, args):
        self.ssh_client(args)

    def dir(self, args):
        self.ssh_client(args)

    def pwd(self, args):
        self.ssh_client(args)

    def charge(self, args):     # 充会员，增加容量
        print('此功能还没有实现')

# client=MYTCPClient(('127.0.0.1', 9004))
# client.run()

# put D:\\GoogleDownload\\python-3.6.4.exe
# put D:\\GoogleDownload\\SourceTreeSetup_1.4.1.exe
# put D:\\GoogleDownload\\Python-3.6.4.tgz
# put D:\\GoogleDownload\\BaiduNetdisk_5.7.2.3.exe
# put D:\\GoogleDownload\\Wireshark-win32-2.4.3.0.exe
# put D:\\GoogleDownload\\BANDIZIP-6.10.0.1-SETUP.EXE
# get python-3.6.4.exe
# get SourceTreeSetup_1.4.1.exe
# get BaiduNetdisk_5.7.2.3.exe
