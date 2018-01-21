import pickle
def alter(file, old_str, new_str):
    """
    替换文件中的字符串
    :param file:文件名
    :param old_str:就字符串
    :param new_str:新字符串
    :return:
    """
    file_data = ""
    with open(file, "r", encoding="utf-8") as f :
        for line in f:
            if old_str in line:
                line = line.replace(old_str,new_str)
            file_data += line
    with open(file, "w", encoding="utf-8") as f:
        f.write(file_data)

# a = 123
# # alter('user_info.txt', 'tsy', 'ttt')
# print(':'.join(["'balance'", str(0)]))
# print(':'.join(["'balance'", str(10000)]))
# # alter('user_info.txt', ':'.join(['passwd', '123456']), ':'.join(["'passwd'", "'" + str(a) + "'"]))
# alter("user_info.txt", ':'.join(["'balance'", str(0)]), ':'.join(["'balance'", str(10000)]))
# a = 'qeqweqwe\n'
# b = 'asdasdsa\n'
# c = 'qweqrvsdgre\n'
# str1 = ''.join([a, b, c])
# print()
# with open('purchase_record.txt', 'a', encoding='utf8') as f:
#     f.write(str1)
L_purchase_record_dispaly = []
# with open('purchase_record.txt','r',encoding='utf8') as f3:
#     for i in f3.readlines():
#         L_purchase_record_dispaly.append(i.strip())
# for i in L_purchase_record_dispaly:
#     print(i)
shopping_cart_history = pickle.load(open('purchase_record.txt', 'rb'))
print(shopping_cart_history)
