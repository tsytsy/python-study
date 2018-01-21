import re

# print(name)
# print(name.strip())#strip 脱掉,只能去掉字符串前面和后面的空格和换行
#
# print(name.split(" ")) #把一个字符串分割为列表类型
# print(len(name))  #字符串长度
#



#字符串截取
# print(name[0:6])
# print(name[:])
# print(name[:8])
# print(name[-1])
# print(name[:-1])
# print(name[0:])
#
# a = "hello,world"
# b = a.replace('world','python')
# print(a)
# print(b)


#字符串连接
# sStr1 = 'strcat'
# sStr2 = ' append'
# sStr1 += sStr2
# print(sStr1)

#查找字符串
# if 'u' in name:
#         print('11111111')
# print(name.index('u'))

#将字符串中的大小写转换
#strlwr(sStr1)
# sStr1 = 'JCstrlwr'
# sStr2 = sStr1.upper()
# #sStr1 = sStr1.lower()
# print(sStr1)


# sStr1 = 'cekjgdklab'
# sStr2 = 'gka'
# nPos = -1
# for c in sStr1:
#     if c in sStr2:
#         nPos = sStr1.index(c)
#         break
# print(nPos)
print(r'^"raw_title":".*"$')
# match = re.search(r'\d+.*\d+.mp4"', '"qweqwe"  "123ewew12312.mp4" "qweqw.mp4"')
# # print(r'\t')
# if match:
#     print('>>>>>', match.group(0))

html = '"raw_title":"巴朗双肩包时尚潮流韩版中学生书包","raw_title":"迪卡侬双肩包男女 KIPSTA"'
tlt = re.findall('"raw_title":".*"', html)
print(">>>>>>>>>>>>>", tlt)