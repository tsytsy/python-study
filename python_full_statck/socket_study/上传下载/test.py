#!/usr/bin/env python
# _*_ coding:utf8 _*_
import random
# def process(size, total_size):
#     percent = size/total_size
#     # print(percent)
#     percent1 = round(percent*100, 2)
#     # print(percent1)
#     NUM_OF_STAR = int(percent*100/2)
#     # print(NUM)
#     print('[%s]%s%%' % ('*'*NUM_OF_STAR, percent1))
# process(52674464, 52674464)

class start:
    def __init__(self):
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
            if hasattr(menu_dic, choose):
                menu_dic[choose]()
            else:
                print('输入错误，请重新选择服务')

    def register(self):
        print('register')
    def login(self):
        pass
    def quit_menu(self):
        exit()
start = start()
