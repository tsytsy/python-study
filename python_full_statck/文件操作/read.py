#用户输入一个网址，打印出网址的服务器列表


http = input("Input the http:")
L = []
flag = False
with open('haproxy.conf', encoding='utf8') as f_read:
    for line in f_read:
        if line.strip() == ' '.join(['backend', http]):
            flag = True
            continue
        if flag:
            if line.startswith('backend'):
                flag = False
                continue
            L.append(line.strip())
for i in L:
    print(i)


