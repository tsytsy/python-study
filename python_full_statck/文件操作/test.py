# f = open('test', 'w+', encoding='utf8')
# data = f.read()
# print(data)

# print(f)
# print(f.readlines())
# count = 0
# for i in f.readlines():
#     if count == 1:
#         print("".join([i.strip(), 'hello\n']))
#     else:
#         print(i)
#     count += 1




# #r+#
# f = open('test', 'r+', encoding='utf8')
# print(f.read())
# f.write('hello中国')
# # f.seek(0)   #读的是字节数
# print(f.read())
#
#
# #w+先覆盖,后写入#
# # print(f.read())
# # f.write('hello中国')
# # f.seek(6)   #读的是字节数
# # print(f.read())
# #
#
# # #a+，不覆盖，直接在后面添加#
# # f = open()

#文件修改

# def modify_file(file, old_content, new_content):
#     with open(file, 'r', encoding='utf8') as f:
#         for line in f.readlines():
#             if old_content in line:

L = []
with open('test', 'r', encoding='utf8') as f:
    for line in f.readlines():
        if '6000' in line:
            line = line.replace('6000', '5800')

        L.append(line)

with open('test', 'w', encoding='utf8') as f:
    for line in L:
        f.write(line)
