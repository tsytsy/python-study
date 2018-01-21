
try:
    print('==========')
    l = [1,2,3]
    # print(x)
    l[1]

    print('============')
except NameError as x:
    print(x)
except ValueError as x:
    print(x)
except Exception as x:
    print(x)

else:
    print('6666')
finally:
    print('finally')