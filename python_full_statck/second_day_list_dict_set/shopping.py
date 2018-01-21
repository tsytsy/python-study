#需求
    # 启动程序后，让用户输入工资，然后打印商品列表
    # 允许用户根据商品编号购买商品
    # 用户选择商品后，检测余额是否够，够就直接扣款，不够就提醒
    # 可随时退出，退出时，打印已购买商品和余额

print("Welcome to Tmall")
print("If you want to quit, please enter a 'q'")
while True:
    salary = input("Please input your salary:").strip()   #输入字符时前面有可能是空格

    if not(salary.isdigit()):                       #'q' or '123qqq'
        if salary == 'q':
            exit()
        else:
            print("your input has characters, try it again")
            continue
    else:
        balance = int(salary)
        product_list = ["iphone", "coffee", "book", "apple"]
        price_list = [5800, 90, 60, 10]
        print("there are our products")
        shopping_list = []
        for i in range(len(product_list)):
            print(i+1, product_list[i], price_list[i])

        while True:
            index = input("Input the number of product you want:")
            if not(index.isdigit()):
                if index == 'q':
                    print("you will exit later")
                    print("Your balance is ", balance)
                    print("there is your shopping list", shopping_list)
                    exit()
                else:
                    print("you choice has characters, please input the number of produces")
                    continue
            else:
                index = int(index)
                if index > len(price_list):
                    print("There is no", index, "product", "please try it again")
                    continue
                else:
                    if balance < price_list[index-1]:
                        print("Sorry,there is enough money for it")
                        continue
                    else:
                        balance = balance - price_list[index-1]
                        shopping_list.append(product_list[index-1])
                        print(product_list[index-1], "has been add the shopping curt")

