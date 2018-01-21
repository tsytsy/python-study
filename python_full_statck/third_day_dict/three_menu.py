# 程序: 三级菜单
#
# 要求:
#
# 打印省、市、县三级菜单
# 可返回上一级
# 可随时退出程序

menu = {
    '北京':{
        '海淀':{
            '五道口':{
                'soho':{},
                '网易':{},
                'google':{}
            },
            '中关村':{
                '爱奇艺':{},
                '汽车之家':{},
                'youku':{},
            },
            '上地':{
                '百度':{},
            },
        },
        '昌平':{
            '沙河':{
                '老男孩':{},
                '北航':{},
            },
            '天通苑':{},
            '回龙观':{},
        },
        '朝阳':{},
        '东城':{},
    },
    '上海':{
        '闵行':{
            "人民广场":{
                '炸鸡店':{}
            }
        },
        '闸北':{
            '火车战':{
                '携程':{}
            }
        },
        '浦东':{},
    },
    '山东':{},
}

while True:
    for i in menu.keys():
        print(i)
    provice = input("input which provice you want to look:")
    if provice in menu.keys():
        while True:   #进入北京
            print('222222', menu[provice].keys())
            for i in menu[provice].keys():
                print("===>", i)  #北京下面的区
            # elif provice == "上海":
            #     print(menu["上海"].keys())
            # elif provice == "山东":
            #     print(menu["山东"].keys())
            city = input("which city you want to look:")
            # print(menu[provice].keys())

            if city in menu[provice].keys():
                while True:    #进入海淀
                    print("333333", menu[provice][city].keys())
                    for i in menu[provice][city].keys():
                        print("=======>", i)  #进入海淀下面的
                    district = input("which district you want to look:")

                    if district in menu[provice][city].keys():
                        while True:
                            print("4444444", menu[provice][city][district].keys())
                            for i in menu[provice][city][district].keys():
                                print('============>', i)
                            company = input('which company you want to look:')
                            if company in menu[provice][city][district].keys():
                                while True:

                                    for i in menu[provice][city][district][company].keys():
                                        print(i)
                                    zi_company = input("which zi_company you want to look:")
                                    if zi_company in menu[provice][city][district][company].keys():
                                        for i in menu[provice][city][district][company][zi_company].keys():
                                            print(i)
                                    elif zi_company == 'q':
                                        exit()
                                    elif zi_company == 'b':
                                        break
                                    else:
                                        continue
                            elif company == 'q':
                                exit()
                            elif company == 'b':
                                break
                            else:
                                continue
                    elif district == 'b':
                        break
                    elif district == 'q':
                        exit()
                    else:
                        continue
            elif city == 'b':
                break
            elif city == 'q':
                exit()
            else:
                continue
    elif provice == 'q':
        exit()
    else:
        continue


