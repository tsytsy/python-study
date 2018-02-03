#!/usr/bin/env python
# _*_ coding:utf8 _*_


import paramiko

transport = paramiko.Transport(('192.168.1.66', 22))
transport.connect(username='root', password='q')

sftp = paramiko.SFTPClient.from_transport(transport)
# 将location.py 上传至服务器 /tmp/test.py
sftp.put(r'D:\workplace\python-study\python_full_statck\homework\HostManage\conf\aaa.py', '/tmp/test.py')
# 将remove_path 下载到本地 local_path
# sftp.get('/etc/passwd', 'passwd')

transport.close()


# D:\\workplace\\python-study\\python_full_statck\\homework\\HostManage\\conf\\aaa.py
# /root/aaa.py