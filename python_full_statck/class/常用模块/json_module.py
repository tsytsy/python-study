import json
'''
json.dumps 会将数据类型转换为json字符串，json字符串和python字符串有区别，python中的字符串可以用单引号或者双引号
表示，但是在json数据类型中，字符串只用双引号表示。
'''

# d = {'1': 1, '2': 2}
# s = json.dumps(d)
# print(s)

i=10
s='hello'
t=(1,4,6)
l=[3,5,7]
d={'name':"yuan"}

json_str1=json.dumps(i)
json_str2=json.dumps(s)
json_str3=json.dumps(t)
json_str4=json.dumps(l)
json_str5=json.dumps(d)

print(json_str1)   #'10'
print(json_str2)   #'"hello"'
print(json_str3)   #'[1, 4, 6]'
print(json_str4)   #'[3, 5, 7]'
print(json_str5)   #'{"name": "yuan"}'

d2 = json.loads(json_str5)
print(d2)

with open('new', 'w') as f:
    f.write(json_str5)

