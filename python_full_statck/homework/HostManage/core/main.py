#!/usr/bin/env python3
# _*_ coding:utf8 _*_

'''
简单的主机管理工具
1. 主机分组
2. 登录后显示主机分组，选择分组后查看主机列表
3. 可批量执行命令，发送文件
4. 主机用户名密码可以不同  # 用于ssh连接，发送命令以及文件

'''
import configparser
import os
import threading
from conf import settings
from conf import common
import time
import paramiko
class HostManage:
    def __init__(self):
        self.username = settings.LOGIN_USERNAME
        self.passwd = settings.LOGIN_PASSWD
        self.login()

    def login(self):
        while True:     # 退出循环还没做
            username = input('username>>:')
            passwd = input('passwd>>:')
            if username == self.username and passwd == self.passwd:
                print('login successful')
                self.computer_group()
                break
            else:
                print('login fail, try it again')

    def computer_group(self):
        conf = configparser.ConfigParser()
        conf.read(settings.HOST_CONF_DIR)
        while True:
            for g in conf.sections():
                print('%s [%s]' % (g, len(conf.options(g))))
            group_choose = input('choose your group like(group 1), enter b to back>>:')
            if group_choose == 'b':
                return
            if group_choose not in common.section_list():
                print('there is no this group, try it again')
                continue
            self.host_list(group_choose)

    def host_list(self, group):
        # print(group)
        groupmem_info = common.read_group_info_dic(group)
        # print(groupmem_info)
        print('{:<10}{:<10}{:<20}'.format('USERNAME', 'PASSWD', 'IP'))
        for dic in groupmem_info:
            print('{:<10}{:<10}{:<20}'.format(dic['username'], dic['passwd'], dic['ip']))

        self.func_interactive(group)

#  '****************************************func choose*********************************'

    def func_interactive(self, group):
        fuc_menu = '''
        1. exec_cmd
        2. send_file
        b. back
        '''
        func_dic = {
            '1': 'exec_cmd',
            '2': 'send_file',
            'b': 'back'
        }
        while True:
            print(fuc_menu)
            func_choose = input('choose your fuc>>:')
            if func_choose == 'b':
                return
            if func_choose not in func_dic:
                print('there is no this function,try it again')
                continue
            func = getattr(self, func_dic[func_choose])
            func(group)

    def exec_cmd(self, group):
        thread_list = []
        cmd = input('input cmd>>:')
        groupmem_info = common.read_group_info_dic(group)
        for dic in groupmem_info:
            t = threading.Thread(target=self.ssh_exec_cmd, args=(dic, cmd,))
            t.start()
            thread_list.append(t)
        for t in thread_list:
            t.join()

    def ssh_exec_cmd(self, dic, cmd):
        # print(dic, cmd)
        ssh = paramiko.SSHClient()
        # 允许连接不在know_hosts文件中的主机
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # 连接服务器
        ssh.connect(hostname=dic['ip'], port=22, username=dic['username'], password=dic['passwd'])
        # 执行命令
        stdin, stdout, stderr = ssh.exec_command(cmd)
        # 获取命令结果

        std = stdout.read()
        sterr = stderr.read()
        result = std if std else sterr
        print('--command [%s] result-------from %s----------' % (cmd, dic['ip']))
        print(result.decode('utf8'))
        print('----------------------------------------------')
        # 关闭连接
        ssh.close()

    def send_file(self, group):
        thread_list = []
        local_file = input('local file path>>:')
        remote_file_path = input('remote file path:>>')
        groupmem_info = common.read_group_info_dic(group)
        for dic in groupmem_info:
            t = threading.Thread(target=self.ssh_send_file, args=(dic, local_file, remote_file_path))
            t.start()
            thread_list.append(t)
        for t in thread_list:
            t.join()

    def ssh_send_file(self, dic, local_file_path, remote_file_path):
        transport = paramiko.Transport((dic['ip'], 22))
        transport.connect(username=dic['username'], password=dic['passwd'])

        sftp = paramiko.SFTPClient.from_transport(transport)
        # 将location.py 上传至服务器 /tmp/test.py
        sftp.put(local_file_path, remote_file_path)
        # 将remove_path 下载到本地 local_path
        # sftp.get('/etc/passwd', 'passwd')

        transport.close()


# D:\\workplace\python-study\\python_full_statck\\homework\\HostManage\\conf\\host_info.conf
# /root/host.conf


