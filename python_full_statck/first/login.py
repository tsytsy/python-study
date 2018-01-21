#编写登录接口，输入用户名，密码，输入正确，则显示欢迎信息，输错三次后锁定#
count = 0
while count < 3:
    #读出已经注册的账号和密码，账号放入user_list，密码放入passwd_list中
    f = open('D:\BaiduNetdiskDownload\\account.txt', 'r', encoding='utf8')
    list1 = f.readlines()
    f.close()
    print(list1)
    user_list = list1[0].strip().split(":")[1].split(",")
    passwd_list = list1[1].strip().split(":")[1].split(",")
    print(user_list)
    #读出已经锁定的账号，放入locked_list中
    f = open('D:\BaiduNetdiskDownload\\hote.txt', 'r', encoding='utf8')
    list2 = f.readlines()
    f.close()
    print('***********', list2)

    locked_list = []
    for lines in list2:
        locked_list.append(lines.replace("\n", ""))

    # print("###################")
    # print(list2)
    # print(locked_list)
    # print(user_list, passwd_list)

    username = input("Input your username:")
    if not(username in user_list):
        print("You have not registered,Please register first")
        break
    else:
        index = user_list.index(username)
        # print(index)
    if username in locked_list:
        print("You have be locked,Please contact the staff")
        break
    user_password = input("Input your password:")

    # print(user_list[index])
    # print("11111111111111111", user_password[index])

    if username == user_list[index] and user_password == passwd_list[index]:
        print("Welcome here")
        break
    else:
        print("Account name or login password is incorrect, please reenter")
        count += 1
        if count == 3:
            print("Please try again later")
            f = open('D:\BaiduNetdiskDownload\hote.txt', 'a', encoding='utf8')
            f.write(username+'\n')
            f.close()
            exit()


#初步了解文件的读写操作
#掌握list的增(append),查(in,index),查list[index]
#掌握字符串的分割split，去除空格和换行符strip
#掌握In关键字查询列表中是否存在项目 if item in list .......