# #1使用while循环输入 1 2 3 4 5 6 8 9 10
#
# count = 0
# L = []
# while count < 10:
#     count += 1
#     if count == 7:
#         continue
#     L.append(count)
# print(L)

#2、求1-100的所有数的和
# s = 0
# for i in range(101):
#     s += i
# print(s)
# s = 0
# count = 0
# while count < 101:
#     s += count
#     count += 1
# print(s)
#3、输出1 - 100内的所有奇数
# for i in range(1, 100):
#     if i % 2 == 0:
#         continue
#     else:
#         print(i)
# count = 1
# while count < 100:
#     if count % 2 == 0:
#         print(count)
#     count +=1
#4、输出 1-100 内的所有偶数
# for i in range(1, 100):
#     if i % 2 == 0:
#         print(i)
#5、求1-2+3-4+5 ... 99的所有数的和
# s = 0
# for i in range(1, 100):
#     if i % 2 == 0:
#         i = 0 - i
#     s += i
# print(s)
#模拟登陆
 #   1. 用户输入帐号密码进行登陆

# while True:
#     account = input("Please input your account:")
#     passwd = input("Please input your passwd:")
#     if account == 'tsy' and passwd == '1t1y':
#         print("Wawa, welcome")
#         break
#     else:
#         print("Sorry,your account or passwd wrong.")

#2. 用户信息保存在文件内,在文本信息内存放多个用户和密码
# L = []
# with open('account_passwd.txt', encoding='utf8') as f:
#     for line in f:
#         L.append(line.strip().split(":")[1])
# user_list = L[0].split(",")
# passwd_list = L[1].split(",")
# while True:
#     account = input("Please input your account:")
#     if account in user_list:
#         passwd = input("Please input your passwd:")
#         if account == account and passwd == passwd_list[user_list.index(account)]:
#             print("Wawa, welcome")
#             break
#         else:
#             print("Sorry,your account or passwd wrong.")
#     else:
#         print("account no exit")



 #3. 用户密码输入错误三次后锁定用户


L = []
user_list = []
passwd_list = []
lock_list = []
with open('account_passwd.txt', encoding='utf8') as f:
    for line in f:
        L.append(line.strip().split(":")[1])
with open('lock.txt', 'r', encoding='utf8') as f:
    for line in f:
        lock_list.append(line.strip())
user_list = L[0].split(",")
passwd_list = L[1].split(",")
count = 0
while count < 3:
    account = input("Please input your account:")
    if account in lock_list:
        print('you have been locked')
        exit()
    if account in user_list:
        passwd = input("Please input your passwd:")
        if account == account and passwd == passwd_list[user_list.index(account)]:
            print("Wawa, welcome")
            break
        else:
            print("Sorry,your account or passwd wrong.")
            count += 1
            if count == 3:
                print("you will be lock,please try it later")
                with open("lock.txt", "a", encoding='utf8') as f:
                    f.write(''.join([account, "\n"]))
    else:
        print("account no exit")
