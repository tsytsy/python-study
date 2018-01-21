


# name = "中国"
# print name, len(name)
# print [name]
#
# uni = name.decode("utf-8")  ##你现在是什么编码------->默认转换成unicode
#
# print uni, len(uni)    #你看到的并不是uinicode , 你看到的是unicode-->你的终端屏幕的编码格式
# print [uni]
#
# gbk = uni.encode('GBK')   #写要转成的目标编码
#
# print gbk, len(gbk)
# print [gbk]
#
# gb2312 = gbk.decode('GBK').encode('utf-8')
# print gb2312, len(gb2312)
# print [gb2312]

# a = 1
# s = "尼古拉斯"
# s2 = u'尼古拉'
# print s
# print [a]
# print repr(s)
# print repr(s2.encode('utf8'))
# # print repr(s.decode('utf8').encode('GBK'))


#python 3

# a = 1
s = "尼古拉斯"
s2 = b'hello'
print(type(s))
print(type(s2))
print(type(s.encode("GBK")))
print(type(s2.decode("utf8")))