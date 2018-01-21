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

current_layer = menu
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
        # print(last_layer)