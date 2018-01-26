import hashlib
# '''
# 摘要算法又称哈希算法、散列算法。它通过一个函数，把任意长度的数据转换为一个长度固定的数据串（通常用16进制的字符串表示）
# 摘要算法就是通过摘要函数f()对任意长度的数据data计算出固定长度的摘要digest，目的是为了发现原始数据是否被人篡改过
# '''
# md5_1 = hashlib.md5()
# md5_2 = hashlib.md5()
# sha3 = hashlib.sha3_256()
# print(md5_1)
# print(md5_2)
# print(sha3)
#
# md5_1.update(b'hello')
# print(md5_1.hexdigest())
# md5_2.update(b'hello')
# print(md5_2.hexdigest())
# print('*'*50)
#
#
# md5_2.update(b'hello')
# print(md5_2.hexdigest())
# n = hashlib.md5()
# n.update(b'hellohello')
# print(n.hexdigest())
#
# print('='*50)
#
# a1 = hashlib.md5()
# a1.update(b'hello')
# print(a1.hexdigest())
# a2 = hashlib.md5(b'eggon')
# a2.update(b'hello')
# print(a2.hexdigest())

def cacl_md5(passwd):
    md5 = hashlib.md5()
    md5.update(bytes(passwd, encoding='utf-8'))
    return md5.hexdigest()

m1 = cacl_md5('bob')
print(m1)
m2 = cacl_md5('123')
print(m2)

# 设计一个验证用户登录的函数，根据用户输入的口令是否正确，返回True或False：
d = {'bob': '9f9d51bc70ef21ca5c14f307980a29d8', '123': '202cb962ac59075b964b07152d234b70'}
def login():
    user_name = input('>>:')
    passwd = input('>>:')
    print(d[user_name])
    print(cacl_md5(passwd))
    if user_name in d and (cacl_md5(passwd) == d[user_name]):
        print(d[user_name])
        return True
    else:
        return False

while True:
    print(login())

