# def worh():
#     for i in range(10):
#         for j in range(10):
#             for k in range(10):
#                 if k == 1:
#                     return i,j,k
#
#
#
# print(worh())

# list1 = [1, 2, 3, 4, 5]
# for x in list1:
#     print(x)
#     if x == 2:
#         break
# else:
#     print("else")



#如何从最里层循环跳出循环
# break_flag = False
# for i in range(10):
#     print("i", i)
#     for j in range(10):
#         print("j", j)
#         for k in range(10):
#             print("k", k)
#             if k == 3:
#                 break_flag = True
#                 break
#         if break_flag:
#             break
#     if break_flag:
#         break

count = 0
break_flag = True
while break_flag:
    print("111")
    while break_flag:
        print("2222")
        while break_flag:
            print("3333")
            count += 1
            if count > 10:
                break_flag = False