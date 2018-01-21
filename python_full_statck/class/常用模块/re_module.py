import re
'''
1. 正则表达式只使用于字符串的模糊查找
2. 字符串的一些绑定方法如，replace和find等都是完全匹配
'''
'''
1. ^$ 这两个元字符匹配的是整个字符串的开头和结尾，如果开头和结尾不匹配，整个字符串就不匹配
2. 字符转义 果你想查找元字符本身的话，比如你查找.,或者*,就出现了问题：你没办法指定它们，因
    为它们会被解释成别的意思。这时你就得使用\来取消这些字符的特殊意义。因此，你应该使用\.和\*。
    当然，要查找\本身，你也得用\\.
3. 字符集[]，表示的是在[]内取一个值，如[123]表示的是在1,2,3中任意一个数字，又比如[a-z]表示的是
    a-z中的任意一个字母，但是需要注意的是，[]字符集中有些元字符的意义已经失去了意义，比如*，？，.
    等等再字符集里面都是普通字符。但是有下面三个元字符还存在特殊的意义
    -：表示范围，[0-9]表示的是任意数字，而不是0，-，9
    \:后面可以接特殊的元字符：[\d]表示的是去任意的一个数字
    ^：表示取反,[^\d]表示去一个非数字的字符
4. .匹配除换行符的任一字符
'''
# ret1=re.findall('李.','李爽\nalex\n李四\negon\nalvin\n李二')
#
# ret2=re.findall('^李.','李爽\nalex\n李四\negon\nalvin\n李二')
#
# ret3=re.findall('李.$','李爽\nalex\n李四\negon\nalvin\n李二')
# print(ret1)
# print(ret2)
# print(ret3)

# ret1=re.findall('李.*','李杰\nalex\n李莲英\negon\nalvin\n李二棍子')
# ret2=re.findall('李.+','李杰\nalex\n李莲英\negon\nalvin\n李二棍子')
#
# ret3=re.findall('(李.{1,2})\n','李杰\nalex\n李莲英\negon\nalvin\n李二棍子') # 设定优先级的原因
#
# # 匹配一个数字包括整型和浮点型
# ret4=re.findall('\d+\.?\d*','12.45,34,0.05,109')
# print(ret1)
# print(ret2)
# print(ret3)
# print(ret4)


# ret=re.findall('c\\t','abc\te')
# print(ret)#[]


# 字符集[]
# # print(re.findall('a[bc]d', 'abdsiyaswqacdqweas'))  #[abc, abd]
# print(re.findall('a[0-9]d', 'a11db2cqeqsafi8ca6dacd')) # [a6d]
# print(re.findall('a[\d]d', 'a11db2cqeqsafi8ca6dacf'))  # [a6d]
# print(re.findall('a[^\d]d', 'a11db2cqeqsafi8ca6dacd')) # [acd]

# 重复元字符 *，+，{}，?
# print(re.findall('ab*cd', 'abbcd abcd acd abbbcd'))
# print(re.findall('ab?cd', 'acd, abcd abbcd abbbcd'))
# print(re.findall('ab+cd', 'acd abcd abbcd abbbcd'))
# print(re.findall('ab{2,3}cd', 'acd abcd abbcd abbbcd'))

# 分组()
'''
1. 只显示分组里的匹配内容
2. 取消分组的优先级使用?:
3. ()于|一起用，[]值可以选择一个值，()可以选择一个组合(ad|cd)
'''
# print(re.findall('(ad)+', 'adadtsy'))
# print(re.findall('(?:ad+)+', 'adadtsy'))

# 管道符 |
# print(re.findall('www\.(baidu|sina)\.com', 'www.baidu.com'))

# \
# print(re.findall('\d+\.?\d*\*\d+\.?\d*', '2*6+45*7+1.4*3-8/4'))
# print(re.findall('\d+\.?\d+\*\d+\.?\d+', '2*6+45*7+1.4*3-8/4'))
# print(re.findall('\d+\*\d+', '2*6+45*7+1.4*3-8/4'))

'''
实现能计算类似 
1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) -
 (-4*3)/ (16-3*2)  )等类似公式的计算器程序

'''
s = '1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) -(-4*3)/ (16-3*2))'
# print(re.search('\(-?\d+[+\-*/]-?\d+\)', s))
# print(re.findall('\d+[*/]*[+\-]*\d+', '1+2*3'))
print(re.findall('\([^()]+\)', s))
