# 程序: 三级菜单
#
# 要求:
#
# 打印省、市、县三级菜单
# 可返回上一级
# 可随时退出程序
# import json
# with open("menu.json", mode="r", encoding="utf-8") as f:
#     menu = json.loads(f.read())
# # L = []

with open('menu.txt', 'r', encoding='utf8') as f:
    menu = eval(f.read())
current_layer = menu
print(menu)
last_layer = []
while True:
    for i in current_layer:
        print(i)
    choice = input("input your choice:")
    if choice == 'b':
        if last_layer:
            current_layer = last_layer[-1]
            last_layer.pop()
        # print(last_layer)
    elif choice == 'q':
        break
    else:
        last_layer.append(current_layer)
        current_layer = current_layer[choice]



# print(str(L))
# print()
# dir1 = dict(L)
# print(dir1)


