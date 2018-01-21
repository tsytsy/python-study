'''
导入包中的模块

'''


# import sys
# print(sys.path)

# 导入包的时候，使用import 包.模块  或者
# import glance.db.models
# glance.db.models.register_models('mysql')



# import 包.模块.属性 错误的
# import 导入模块的时候.左边必须是包
# import glance.db.models.register_models
# glance.db.models.register_models('mysql')


# 正确
# from glance.db import models
# models.register_models('mysql')


# 需要注意的是from后import导入的模块，必须是明确的一个不能带点，
# 否则会有语法错误，如：from a import b.c是错误语法
# from glance.db import models.register_modles
# register_models('mysql')


# from glance.db.models import register_models
# register_models('mysql')


'''
导入包
只执行包的__init__.py文件
'''
# from glance.api import policy
# #import glance.api


'''
import glance.api 和 import glance.api.policy 的区别
1. 左边导入的是包，导入包只做了一件事情，那就是执行包内的__init__文件，如果__init__文件是空的化，那么无法执行这个
police下的任何功能，
    右边这个语句右两个意思，a. 导入包内的__init__.py文件 b. 明确导入了police模块，且police模块的名字空间的
    指针为glance.api.policy,即如果要调用policy模块下的属性，必须通过glance.api.policy.属性去  调用
'''
# import glance.api
# glance.api.policy.get()
# print(globals())

'''
from glance.api import * 和 from glance.api import policy的区别
1. 左边这个是引入api下包内的__init__.py文件内的所有属性，并不是glance.api下的所有模块
2. 右边这个是调用glance.api下的police模块
'''
# from glance.api import policy
#
# policy.get()

# from glance.api import *
# print(globals())
# print(x, y)
# print(policy)

# import glance
# glance.cmd.manage.main()

# str1 = '''
#
#                    _ooOoo_
#                   o8888888o
#                   88" . "88
#                   (| -_- |)
#                   O\  =  /O
#                ____/`---'\____
#              .'  \\|     |//  `.
#             /  \\|||  :  |||//  \
#            /  _||||| -:- |||||-  \
#            |   | \\\  -  /// |   |
#            | \_|  ''\---/''  |   |
#            \  .-\__  `-`  ___/-. /
#          ___`. .'  /--.--\  `. . __
#       ."" '<  `.___\_<|>_/___.'  >'"".
#      | | :  `- \`.;`\ _ /`;.`/ - ` : | |
#      \  \ `-.   \_ __\ /__ _/   .-` /  /
# ======`-.____`-.___\_____/___.-`____.-'======
#                    `=---='
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#           .............................................                    佛祖镇楼                  BUG辟易
#           佛曰:
#                   写字楼里写字间，写字间里程序员；
#                   程序人员写程序，又拿程序换酒钱。
#                   酒醒只在网上坐，酒醉还来网下眠；
#                   酒醉酒醒日复日，网上网下年复年。
#                   但愿老死电脑间，不愿鞠躬老板前；
#                   奔驰宝马贵者趣，公交自行程序员。
#                   别人笑我忒疯癫，我笑自己命太贱；
#                   不见满街漂亮妹，哪个归得程序员？
# */
#
# '''
# print(str1)

# user_data = {
#     'account_id':None,
#     'is_authenticated':False,
#     'account_data':None
#
# }

# def change():
#     user_data['is_authenticated'] = True
#     x = 1
#
# print(id(user_data))
# print(id(user_data['is_authenticated']))
# print('---------------------------------')
# change()
# print(id(user_data))
# print(id(user_data['is_authenticated']))




