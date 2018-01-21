import logging
import sys_module
def func():
    print('from log')
def func1():
    print('from log')
'''
1.  默认情况下Python的logging模块将日志打印到了标准输出中，且只显示了大于等于WARNING级别的日志，这说明默认的
    日志级别设置为WARNING（日志级别等级CRITICAL > ERROR > WARNING > INFO > DEBUG），默认的日志格式为
    日志级别：Logger名称：用户输出消息。
'''
# 配置 1. configure
# logging.basicConfig(level=logging.DEBUG,
#                     format='%(asctime)s [%(lineno)d] [%(levelname)s] %(message)s ',
#                     datefmt='%Y-%m-%d %H:%M:%S',
#                     filename='log',
#                     filemode='a'
#                     )
#
# # 默认的:默认的日志打印级别是warning，打印格式也是默认的
# logging.debug('debug message')
# logging.info('hello')

# 2. 配置二，logger对象
logger = logging.getLogger()
# print(logger)
# print(logger.__dict__)
# print(logger.name)
# print(logger)

logger.debug('logger debug message')
logger.info('logger info message')
logger.warning('logger warning message')
logger.error('logger error message')
logger.critical('logger critical message')
print(sys_module.x)

