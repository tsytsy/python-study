


# name = "�й�"
# print name, len(name)
# print [name]
#
# uni = name.decode("utf-8")  ##��������ʲô����------->Ĭ��ת����unicode
#
# print uni, len(uni)    #�㿴���Ĳ�����uinicode , �㿴������unicode-->����ն���Ļ�ı����ʽ
# print [uni]
#
# gbk = uni.encode('GBK')   #дҪת�ɵ�Ŀ�����
#
# print gbk, len(gbk)
# print [gbk]
#
# gb2312 = gbk.decode('GBK').encode('utf-8')
# print gb2312, len(gb2312)
# print [gb2312]

# a = 1
# s = "�����˹"
# s2 = u'�����'
# print s
# print [a]
# print repr(s)
# print repr(s2.encode('utf8'))
# # print repr(s.decode('utf8').encode('GBK'))


#python 3

# a = 1
s = "�����˹"
s2 = b'hello'
print(type(s))
print(type(s2))
print(type(s.encode("GBK")))
print(type(s2.decode("utf8")))