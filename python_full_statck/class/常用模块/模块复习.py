# import sys
# import os
# import time_module
# import sys_module
'''
1. 什么是模块?模块的作用是什么?
    模块说白了就是一个py文件，当需要这个文件中的函数，或者类或者属性时，直接从这个文件里面调用。
    模块分为三种：a。标准模块  b.第三方模块   c.自定义模块  （官方写的，大牛写的和你写的）
    文件如何找到一个模块的?
    先从内存中找------->然后从解释器內建模块中找------>最后从路径中找
    第一次导入模块时会做三件事情：a.为导入的文件创建名字空间  b. 执行导入模块  c. 创建模块名变量
2. 常见的模块
3. 自定义模块
4. 什么是包?包的作用是什么?

'''

# sys
'''
sys模块包含了与Python解释器和它的环境有关的函数。
同一级目录下可以导入
sys.path 中的这意味着你可以直接输入位于当前目录的模块。否则，你得把你的模块放在sys.path所列的目录之
一,但是这个是满足不了生产要求的，因为在生产环境中不可能只有一个文件夹，在一个项目文件中，有多个文件夹，不同的
文件夹存放不同功能的py文件，而且文件夹之间需要相互调用，所以这种同一个目录下的调用是不够用的。需要跨
文件调用。(包于包之间的调用)
'''
# print(__file__)
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# sys.path.append(BASE_DIR)
# print(sys.path)
# print(sys.modules)  #


# 包
'''
包的本质就是一个文件夹，那么文件夹唯一的功能就是将文件组织起来随着功能越写越多，我们无法将所以功能都放到一个文件中，
于是我们使用模块去组织功能，而随着模块越来越多，我们就需要用文件夹将模块文件组织起来，以此来提高程序的结构性和可维护性

1. 导入包的本质是在导入包内的__init__.py文件
2. 
'''


import datetime
import random
'''
1. 随机生成一个数
    小数：random.random() 生成一个[0,1)的小数
         random.uniform(a, b)生成一个[a,b）的小数 
    整数：random.randint(a, b)生成一个[a,b]的整数
         random.randrange(a, b)生成一个[a,b)的整数
2. 从序列中选择一个元素
    random.choice(seq)
   从序列中选择k个元素
    random.sample(seq,k)
    Chooses k unique random elements from
3. 注意事项
在random模块中没有随机生成字母的函数，可以从choice中去生成一个随机字母函数
'''
# def alp_random(num_choice=2):
#     if num_choice not in range(0, 3):
#         raise ValueError('num need in [0,2]')
#     if num_choice == 0:
#         'choose lower alph'
#         x = chr(random.randint(97, 122))
#     if num_choice == 1:
#         'choose upper alp'
#         x = chr(random.randint(65, 90))
#     if num_choice == 2:
#         'choose a alp include upper and lower'
#         x1 = chr(random.randint(97, 122))
#         x2 = chr(random.randint(65, 90))
#         x = random.choice([x1, x2])
#     return x
# import my_func
#生成一个6位的随机验证码（验证码中只有数字和字母）

# def v_code():
#     s = ''
#     for i in range(6):
#         alp = my_func.alp_random()
#         num = str(random.randint(0, 9))
#         s += random.choice([alp, num])
#     return s
# print(v_code())
# print(alp_random())

# print(random.uniform(1, 3))


import os
'''
os模块
'''
# # path = os.path.abspath(__file__)
# path1 = r'C:\Users\jie\root'
# if not os.path.exists(path1):
#     os.mkdir(path1)
# os.path.join(path1, 'aaa')
# with open(os.path.join(path1, 'aaa'), 'w', encoding='utf-8') as f:
#     f.write('lyt, I love it')
# os.path.join()


#方式一：推荐使用
import os
#具体应用
# import os,sys
# possible_topdir = os.path.normpath(os.path.join(
#     os.path.abspath(__file__),
#     os.pardir, #上一级
#     os.pardir,
#     os.pardir
# ))
# print(possible_topdir)
# sys.path.insert(0,possible_topdir)


#方式二：不推荐使用
# os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

#
# print('[%-15s]' %'#')
# print('[%-15s]' %'##')
# print('[%-15s]' %'###')
# print('[%-15s]' %'####')
#
# print('%s%%' %(100)) #第二个%号代表取消第一个%的特殊意义
#
# #可传参来控制宽度
# print('[%%-%ds]' %50) #[%-50s]
# print(('[%%-%ds]' %50) %'#')
# print(('[%%-%ds]' %50) %'##')
# print(('[%%-%ds]' %50) %'###')
#
#
# #=========实现打印进度条函数==========
# import sys
# import time
#
# def progress(percent,width=50):
#     if percent >= 1:
#         percent=1
#     show_str=('[%%-%ds]' %width) %(int(width*percent)*'#')
#     print('\r%s %d%%' %(show_str,int(100*percent)),file=sys.stdout,flush=True,end='')
#
#
# #=========应用==========
# data_size=1025
# recv_size=0
# while recv_size < data_size:
#     time.sleep(0.1) #模拟数据的传输延迟
#     recv_size+=1024 #每次收1024
#
#     percent=recv_size/data_size #接收的比例
#     progress(percent,width=70) #进度条的宽度70



# 打印进度条
#
# print('[%-15s]' % '#')
# print('[%-15s]' % '##')
# print('[%-15s] %s%%' % ('###', 15))
# print('[{}]'.format('#'))

# import time
# def process(percent):
#     if percent < 1:
#         percent = 1
#     print('[%-100s] %s%%' % ('#' * percent, percent))
#
# def get_process(transfer_size, total_size):
#     percent = round((transfer_size/total_size*100))
#     return percent
#
# total_size = 50
# size = 0
# while size < total_size:
#     time.sleep(1)
#     process(get_process(size, total_size))
#     size += 1


# import json


# d = 'str11111'
# j1 = json.dumps(d)
# print(type(j1))
# with open('log1', 'w') as f:
#     f.write(j1)

# json.dump(d, open('log2', 'w'))

# f = open('log1', 'r')
# # j2 = json.loads(f.read())
# j3 = json.load(f)
# print(j3)

import logging

import logging

# logging.basicConfig(filemode='w',
#                     filename='access.log',
#                     format='%(asctime)s %(levelname)s %(message)s',
#                     datefmt='%Y-%m-%d %X',
#                     level=10
#                     )
#
# logging.debug('调试debug')
# logging.info('消息info')
# logging.warning('警告warn')
# logging.error('错误error')
# logging.critical('严重critical')

'''
WARNING:root:警告warn
ERROR:root:错误error
CRITICAL:root:严重critical
'''

def MyLogger():
    logger = logging.getLogger()
    fm = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')

    fh = logging.FileHandler('accesslog')
    sh = logging.StreamHandler()
    fh.setFormatter(fm)
    sh.setFormatter(fm)
    logger.addHandler(fh)
    logger.addHandler(sh)
    logger.setLevel(10)
    return logger


logger = MyLogger()

logger.debug('logger debug message')
logger.info('logger info message')
logger.warning('logger warning message')
logger.error('logger error message')
logger.critical('logger critical message')

#
# import my_func
# logger = my_func.MyLogger()
# logger.debug('hello')