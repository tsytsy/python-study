import os
'''
1. 获取当前工作目录 os.getcwd()
2. 改变当前的工作目录    os.chdir(path)
3. 生成多级递归目录 os.makedir('dir1/dir2')
4. 若目录为空，则删除，并递归到上一级目录，如若也为空，则删除，依此类推   os.removedirs('path')
5. 生成单级目录   os.mkdir('dirname')
6. 删除多级目录   os.rmdir('dirname')
7. 删除文件     os.remove()
8. 列出指定目录下的所有文件和子目录，包括隐藏文件，并以列表方式打印     os.listdir(path)
9. 删除一个文件   os.remove(path)
10. 重新命名文件或者目录  os.rename('old_name', 'new_name')
11. 输出操作系统特定的路径分隔符，win下为"\\",Linux下为"/"    os.sep
12. 如果path存在，返回True；如果path不存在，返回False       os.path.exists(path)  
13. 查看文件信息(上次访问时间，文件大小等)    os.stat
14. 路径拼接    os.path.join(path1, path2)

'''

# # os.getcwd()
# path = os.chdir(r'D:\python_workplace')
# # print(os.getcwd())
# # os.makedirs('aaa/bbb')
# # os.removedirs(r'D:\python_workplace')
# # os.remove(r'D:\python_workplace')
# # print(os.curdir)
# # os.removedirs(r'D:\python_workplace\aaa\bbb')
# # os.mkdir('aaa')
# print(os.listdir(path))
# # os.rename('test.py', 'test1.py')
# print(os.stat(r'D:\python_workplace\test1.py'))
# print(os.system('dir'))
abs_path = os.path.abspath('os_module.py')
print(os.path.split('os_module.py'))
print(os.path.split(abs_path))
print(os.path.dirname(abs_path))
print(os.path.basename(abs_path))

s1 = 'D:\\python_workplace\\python_full_statck\\class\\常用模块'
s2 = 'os_module.py'
print(os.path.join(s1, s2))
