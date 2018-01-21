#coding:utf8

#运行环境:win10 64 pycharm3.6.2

#在一级菜单一共有三个服务，选择不同的服务进入不同的子菜单,每个子菜单对应一个文件，文件必须是字典的格式，不然会出错(感觉是个bug)
#1	商品信息
#2	用户信息
#3	购物记录
#在子菜单中实现功能，如在商品信息中实现商品分类，商品信息显示， 允许用户多次购买，每次可购买多件，余额不足时进行提醒，退出这个子界面时，会打印购买记录，
            #且将此次购买的商品放入购买记录的文件中，方便下次查看
#在用户信息中，实现用户信息的查看一级用户信息的更改以及余额充值，信息更改后相应的文件会立即更改
#在历史菜单，可以查看购买记录


#需要注意的而是,在最下层的菜单（字典没有嵌套的那一层，如购买信息，用户信息）输入q退出最下层，之后在choice中选择b回到上一层，选择q退出，不打印东西，
        #因为在退出各个子菜单中已经打印了



#定义函数alter(),用来改变文件内容

def alter(file, old_str, new_str):
    """
    替换文件中的字符串
    :param file:文件名
    :param old_str:就字符串
    :param new_str:新字符串
    :return:
    """
    file_data = ""
    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            if old_str in line:
                line = line.replace(old_str, new_str)
            file_data += line

    with open(file, "w", encoding="utf-8") as f1:
        f1.write(file_data)
        f1.flush()

#从用户信息文件user_info.txt中读取余额信息。
with open("user_info.txt", 'r', encoding='utf8') as f3:
    for lines in f3.readlines():
        if 'balance' in lines.strip():
            balance = int(lines.split(':')[1].split(',')[0])

#将文件中的字符串转成列表，分级显示商品以及用户信息，购买记录
with open('product_list.txt', 'r', encoding='utf8') as f:
    product = eval(f.read())
with open("user_info.txt", 'r', encoding='utf8') as f2:
    user_info = eval(f2.read())
with open('purchase_record.txt', 'r', encoding='utf8') as f3:
    L_purchase_record_dispaly = eval(f3.read())

lever1 = {'商品信息': product, '用户信息': user_info, '购物记录': L_purchase_record_dispaly}
current_layer = lever1
purchase_list = []
last_layer = []
first_server = ''   #用此字符串来选择
flag = True
old_passwd = ''
old_balance = 0
while True:
    count0 = 0
    if not(last_layer):
        flag = True
    count1 = 0
    for i in current_layer:
        if type(current_layer[i]) is dict:
            print("".join([str(count1 + 1), '\t', i]))
            count1 += 1
        if i == list(current_layer.keys())[-1]:      #确保是最后一个，等出循环时，进入choice选择
            if not(type(current_layer[i]) is dict):  #判断是否还有嵌套字典，如果没有,则为最底层的字典，显示商品信息以及用户信息
                while True:
                    if first_server == '商品信息':
                        purchase_num = []
                        count2 = 0
                        for i in current_layer:
                            print("".join([str(count2 + 1), '\t', i, '\t', "该商品还剩下%s件，单价为%s" % (current_layer[i][0], current_layer[i][1])]))
                            count2 += 1
                        product_choice = input("输入你想要买的商品：")
                        if product_choice in current_layer.keys():
                            purchase_num.append(product_choice)
                            product_num = input('需要购买几件：')
                            purchase_num.append(product_num)
                            purchase_num.append(current_layer[product_choice][1])
                            purchase_list.append(purchase_num)
                            current_layer[product_choice][0] -= int(product_num)
                            if current_layer[product_choice][1]*int(product_num) > balance:
                                print("你的余额不足")
                                continue
                            balance -= current_layer[product_choice][1]*int(product_num)
                        elif product_choice == 'q':
                            L_purchase_record = []
                            print('你的余额为%s' % balance)
                            print('你的购物车中有下列商品'.center(30, '*'))
                            count4 = 1
                            for j in purchase_list:
                                str4 = ' '.join([str(j[1]), str(j[2]), str(int(j[1])*int(j[2]))])
                                str3 = ':'.join(["'"+str(j[0])+"'", "'"+str4+"'"])
                                L_purchase_record.append(str3)
                                print('\t'.join([str(count4), str(j[0]), str(j[1]), str(j[2]), str(int(j[1])*int(j[2]))]))
                                count4 += 1
                            print("*".center(30, '*'))
                            print("\n你的当前位置")
                            count3 = 1
                            for k in current_layer:
                                print("".join([str(count3), '\t', k]))
                                count3 += 1
                            for k in L_purchase_record:
                                alter('purchase_record.txt', '}', k+",\n}")
                            break
                    elif first_server == '用户信息':
                        print('用户信息'.center(30, '*'))
                        print('账号\t', '密码\t', '余额')
                        for k in current_layer:
                            print(current_layer[k], end='\t')
                            if k == 'account':
                                old_account = current_layer[k]
                            if k == 'passwd':
                                old_passwd = current_layer[k]
                            if k == 'balance':
                                old_balance = current_layer[k]
                        char = input("\n\n输入yes可以进行充值，输入t修改密码，输入q退出当前界面:")
                        if char == 'yes':
                            charge = input('充值金额：')
                            new_balance = int(old_balance) + int(charge)
                            # old_balance = new_balance
                            alter("user_info.txt", ':'.join(["'balance'", str(old_balance)]),
                                  ':'.join(["'balance'", str(new_balance)]))
                            current_layer['balance'] = new_balance
                        elif char == 't':
                            new_passwd = input("输入你的新密码:")
                            alter('user_info.txt', ':'.join(["'passwd'", "'" + str(old_passwd) + "'"]),
                                  ':'.join(["'passwd'", "'" + str(new_passwd) + "'"]))
                            current_layer['passwd'] = new_passwd
                        elif char == 'q':
                            count3 = 0
                            print('用户信息'.center(30, '*'))
                            print('账号\t', '密码\t', '余额')
                            for k in current_layer:
                                print(current_layer[k], end='\t')
                            print('\n\n')
                            count6 = 1
                            for k in last_layer[-1]:
                                print("%-8s%-8s" % (count6, k))
                                count6 += 1
                            break
                    elif first_server == '购物记录':
                        L1 = []
                        with open('purchase_record.txt', 'r', encoding='utf8') as f3:
                            L_purchase_record_dispaly = eval(f3.read())
                        print("%-10s%-10s%-10s%-10s" % ('商品名称', '数量', '价格', '花费'))
                        for k in L_purchase_record_dispaly:
                            L1 = L_purchase_record_dispaly[k].split(" ")
                            print("%-10s%-10s%-10s%-10s" % (k, L1[0], L1[1], L1[2]))
                        a = input('请输入q退出当前界面>>')
                        if a == 'q':
                            count6 = 1
                            for k in last_layer[-1]:
                                print("%-8s%-8s" %(count6, k))
                                count6 += 1
                            flag = True
                            count0 = 0
                            current_layer = lever1
                            last_layer = []
                            break
    choice = input("选择你要的服务：")
    if choice in current_layer:
        if flag:
            if count0 == 0:
                first_server = choice
                flag = False
        count0 += 1
        # print(first_server)
        last_layer.append(current_layer)
        current_layer = current_layer[choice]
    elif choice == 'b':
        if last_layer:
            current_layer = last_layer[-1]
            last_layer.pop()
    elif choice == 'q':
        break