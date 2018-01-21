#_*_ coding:utf-8 _*_

#一：编写函数，（函数执行的时间是随机的）,要求登录成功一次，后续的函数都无需再输入用户名和密码
#编写装饰器，为多个函数加上认证功能，要求登录成功一次，在超时时间内无需重复登录，超过了超时时间，则必须重新登录

# import time
# import os
#
#
# def modify_file(file, old_content, new_content):
#     with open(file, 'r', encoding='utf8') as f1, open('file.bak', 'w', encoding='utf8') as f2:
#         for line in f1.readlines():
#             if old_content in line:
#                 line = line.replace(old_content, new_content)
#             f2.write(line)
#     os.remove(file)
#     os.rename('file.bak', file)
#
#
# def readinfo(file):
#     with open(file, 'r', encoding='utf8') as f:
#         d = eval(f.read())
#         return d
#
#
# def timmer(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         res = func(*args, **kwargs)
#         stop_time = time.time()
#         print('running time is {}'.format(stop_time-start_time))
#         return res
#     return wrapper
#
#
# info = readinfo('info.txt')
# d = {'last_login_time': 0.0}
# time1 = 600
# def auth(func):
#     def wrapper(*args, **kwargs):
#         # print(last_login_time)
#         current_time = time.time()
#         interval_time = current_time-d['last_login_time']
#         if not info['login'] or interval_time > time1:
#             name = input('name:').strip()
#             passwd = input('passwd:').strip()
#             if name == info['name'] and passwd == info['passwd']:
#                 # last_login_time = time.time()
#                 print('login successful')
#                 info['login'] = True
#                 d['last_login_time'] = time.time()
#         res = func(*args, **kwargs)
#         return res
#     return wrapper
#
# @auth
# # @timmer   #foo = timmer(foo)
# def foo():
#     print('Welcome main page')
#
#
# @auth
# def home():
#     print('Welcome home page')
#
#
# home()
# foo()
import requests
import os
# #六：编写下载网页内容的函数，要求功能是：用户传入一个url，函数返回下载页面的结果
# 题目五编写装饰器，实现缓存网页内容的功能：
#具体：实现下载的页面存放于文件中，如果文件内有值（文件大小不为0），就优先从文件中读取网页内容，否则，就去下载，然后存到文件中#

# path = 'cache.txt'
# def make_cache(func):
#     def wrapper(*args, **kwargs):
#         if os.path.exists(path):
#             if os.path.getsize(path):
#                 with open(path, 'r', encoding='utf8') as f:
#                     return f.read()
#             else:
#                 print('It is empty')
#         else:
#             # os.mkdir(path)
#             with open(path, 'w', encoding='utf8') as f:
#                 f.write(func(*args, **kwargs))
#     return wrapper
#
#
# @make_cache
# def getHTTPText(url):   #getHTTPText = make_cache(getHTTPText)
#     return requests.get(url).text
#
#
# res = getHTTPText('http://www.baidu.com')
#
# print(res)

#九 编写日志装饰器，实现功能如：一旦函数f1执行，则将消息2017-07-21 11:12:11 f1 run写入到日志文件中，日志文件路径可以指定
#注意：时间格式的获取
import time

path = 'cache.txt'
def log(func):
    def wrapper(*args, **kwargs):
        with open(path,'a', encoding='utf8') as f:
            f.write('\n'+time.strftime('%Y-%m-%d %X'))
        func(*args, **kwargs)
    return wrapper

@log    # f1 = log(f1)
def f1():
    print('from f1')


f1()