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
        shopping_list = {}
        # count_list = {}
        # for count in product_list:
        #     count_list[count+"_count"] = 0
        # print(count_list)

        for i in range(len(product_list)):
            print(i+1, product_list[i], price_list[i])

        while True:
            index = input("Input the number of product you want:")
            if not(index.isdigit()):
                if index == 'q':
                    print("you will exit later")
                    print("Your balance is ", balance)
                    print("there is your shopping list", shopping_list)
                    print("%-5s %-5s, %-5s %-5s %-5s" % ('id', 'product', 'count', 'pricet', 'cost'))
                    for i in shopping_list:
                        print("%-5d %-5s %-5d %-5d %-5d" % (i, shopping_list[i][0],
                            int(shopping_list[i][1]), int(shopping_list[i][2]), int(shopping_list[i][1]*shopping_list[i][2])))
                    # for i range(len(shopping_list))
                    # shopping_list[index] = [product_list[index - 1], count, price_list[index - 1], total_price]
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
                        print("Sorry,there is not enough money for it")
                        continue
                    else:
                        balance = balance - price_list[index-1]
                        # for count in product_list:
                        #     count_list[count + "_count"] = 0
                        count_name = product_list[index - 1] + "_count"
                        if index in shopping_list:
                            shopping_list[index][1] += 1
                        else:
                            shopping_list[index] = [product_list[index-1], 1, price_list[index-1]]
                            print("111111111111", shopping_list)
                        print(product_list[index-1], "has been add the shopping curt")


