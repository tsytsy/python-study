#
# import random
#
# secret = random.randint(0, 99)
# guess_time = 0
# while True:
#     guess_time += 1
#     user_guess = int(input("Input your guess:"))
#     if user_guess > secret:
#         print("Try smaller")
#     elif user_guess < secret:
#         print('Try it bigger')
#     else:
#         print('You got it')
#         break
#     if guess_time % 3 == 0:
#         iscontinue = input("Do you want to continue:yes or No?")
#         if iscontinue == "yes":
#             continue
#         elif iscontinue == "No":
#             break
#
# print('The secret is ', secret)
#
# print('The guess_time is ', guess_time)
#
# '''
# score=int(input('please input a your score:'))
# if score > 90:
#     print('A')
# if(80 < score < 90):
#     print('B')
# if(score < 80):
#     print('C')
# '''
d = '{"key1": {1: "1", 2: "2"}, "key2": 2}'
print(d)
print(type(d))
d1 = eval(d)
print(d1)
print(type(d1))


d2 = '''{
    '水果':{
        '苹果':[100,5],
        '橘子':[50,2],
        '香蕉':[60,4],
        },
    '生活用品':{
        '蚊香':[100,2],
        '卫生纸':[200,2],
        '运动鞋':[20,200]
        },
    '书籍':{
        '科技类':{
            '人工智能':[100,60],
            '互联网+':[50,60]
        },
        '魔幻类':{
            '指环王':[100,50],
            '魔戒':[1000,60]
            }
        }
}'''
print(d2)