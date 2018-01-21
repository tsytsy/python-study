with open('menu.txt', 'r', encoding='utf8') as f:
    menu = eval(f.read())
# print(menu)
current_layer = menu
last_layer = []
while True:
    for line in current_layer:
        print(line)
    choice = input("Please input your choice:")
    if choice in current_layer:
        last_layer.append(list(current_layer.keys()))
        current_layer = current_layer[choice]
        # print(last_layer)
    elif choice == 'b':
        if last_layer:
            current_layer = last_layer[-1]
            last_layer.pop()
            # print(last_layer)
    elif choice == 'q':
        break
    else:
        continue
