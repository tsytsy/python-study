#!/usr/bin/env python
# _*_ coding:utf8 _*_


import configparser
#
# config = configparser.ConfigParser()
#
# config["DEFAULT"] = {'ServerAliveInterval': '45',
#                       'Compression': 'yes',
#                      'CompressionLevel': '9',
#                      'ForwardX11':'yes'
#                      }
#
# config['bitbucket.org'] = {'User':'hg'}
#
# config['topsecret.server.com'] = {'Host Port':'50022','ForwardX11':'no'}
#
# with open('example.ini', 'w') as configfile:
#
#    config.write(configfile)

import configparser

config = configparser.ConfigParser()

#---------------------------查找文件内容,基于字典的形式

print(config.sections())        #  []

aa = config.read('example.ini')
print(aa)

# print(config.sections())        #   ['bitbucket.org', 'topsecret.server.com']
# # print(config.default_section)
# print(config.items('bitbucket.org'))
#
# print('bytebong.com' in config) # False
# print('bitbucket.org' in config) # True
# opts = config.options
#
print(config['bitbucket.org']["user"])  # hg
#
print(config['DEFAULT']['Compression']) #yes
#
print(config['topsecret.server.com']['ForwardX11'])  #no
#
#
print(config['bitbucket.org'])          #<Section: bitbucket.org>
#
for key in config['bitbucket.org']:     # 注意,有default会默认default的键
    print(key)
#
print(config.options('bitbucket.org'))  # 同for循环,找到'bitbucket.org'下所有键
#
print(config.items('bitbucket.org'))    #找到'bitbucket.org'下所有键值对
#
# print(config.get('bitbucket.org','compression')) # yes       get方法取深层嵌套的值



