#1. for 循环
#for循环的工作原理
#1：执行in后对象的dic.__iter__()方法，得到一个迭代器对象iter_dic
#2: 执行next(iter_dic),将得到的值赋值给k,然后执行循环体代码
#3: 重复过程2，直到捕捉到异常StopIteration,结束循环

#2. bool值为False的情况有如下几种情形
 '''
 空字符，空列表，空元组，空字典，空集合,0，None, 条件比较
 '''
 bool('')
 bool([])
 bool({})
 bool(())
 bool(0)
 bool(None)
 bool(2 < 1)
 
#3. 可迭代对象：字符串''，列表[]，元组()，字典{key-values}，集合{}，生成器generator，迭代器
'''
内置函数中许多函数的参数都是可迭代对象，可迭代对象可以是以上的几种形式之一，但是基本上调用的形式
都是通过将可迭代对象通过__iter__函数转为迭代器，迭代器有__next__方法，内置函数在调用时每一次都使用一个
next方法取得下一个值，然后进行进一步的处理。
'''
#all()函数将可迭代对象中的每一个值进行bool()运算，然后将这些值全部进行与运算，如果有一个值为False,那么整个值False
all([1,2,3,4])----->True
all([1,2,3,0])----->False
any([0,[],{},None])------>False
any([1,0,[]])-------->True

#4. max的使用：1.参数为可迭代对象  2. 参数为多个参数,其中的参数可以为各个类型，如列表
'''
典型应用：可以在字典中找到value值最大的那个，并且返回key值，模拟数据库的实现
'''
max([0,1,2,3])
max([1,2,3],[1])
max([1,-2],key=abs)
max([1,2],[1,2,3],key=lambda x:x[1])

salaries={
    'egon':3000,
    'alex':100000000,
    'wupeiqi':10000,
    'yuanhao':250
}
max(salaries,key=lambda x:salaries[x])

#5. 对property的理解
'''
类或者对象的许多属性的许多属性都不能随意改变，有的属性只能够进行读，有些属性可以进行修改
property的作用就是说将一个函数变成一个属性，常见的使用场景为，类中的私有属性外部不能直接通过属性名称访问
通常的做法是利用一个函数getx()接口，让用户获得属性值，此时这是个函数，但是我们可以将程序简单化，将这个函数变成一个属性，下次调用时直接
使用函数名称就可以调用了
'''

class C:
	def __init__(self):
		self.__money = 0
	@property
	def money(self):
		return self.__money
	def charge(self,values)
		self__money = values
		
c = C()
print(c.money)  #像操作变量一样操作函数

#6. 可调用对象:后面加上()可以运行的就是可调用对象。比如函数，类等等都是可调用对象
def func():
	pass

callable(func)   #True

class Foo:
	pass

callable(Foo)  #True

#7 可迭代对象   迭代器
'''
可迭代对象就是对象具有__iter__方法就是可迭代对象：比如 list
迭代器：迭代器对象就是有__next__方法，比如生成器函数
'''
from collections import Iterable, Iterabor
def count():
    N = 0
    while True:
        yield N
        N += 1
g = count()
g.__next__()	#有这个方法，表明生成器函数生成的是一个迭代器。
next(g)

isinstance(g, Iterabor)   #True


isinstance([],Iterable)	#True


#8 import 的几种用法
'''
1. import module_name
	导入的是整个模块
2. from ... import ....
	
3. 注意事项
	导入包和导入模块是不一样的，导入包只是执行了包里面的__init__.py文件，
	如import package，只是导入了package/__init__.py文件，如果__init__.py不把模块加入
	到init文件中，导入模块不会成功
	导入模块则是建行整个模块的内容全部导入到当前文件夹，掉用模块的属性，只需要加上
	模块名称.属性名称就可以了。
'''

# 对项目目录的理解
'''
1. 在conf文件目录下存放各种配置文件，如settings.py模块下存放一些变量值
2. 
'''


# git 理解
'''
使用git可以比喻做你开始玩一把闯关游戏中的存档过程。
添加远程仓库：git remote add origin git@github.com:tsytsy/python-study.git
应该是 git remote add <name> <url>
其中，name 表示你要给这个远程库起的名字，url 表示这个库的地址

1. git init 初始化了一个存放存档的目录
2. git add  将需要存档的关卡加入到git目录。
3. git commit  添加一个存档记录，且对记录进行说明，如第一关关卡
4. git log 保存你所有的存档记录，你可以从这里看到你存档的所有关卡
5. git reset --hard commit_num 加入我对每一关都进行一个存档，当我玩到最后一关时，我觉得太难了
我想玩第一关找一下自信，所以我就打开git log，找到第一关的标识(commit_num)，然后打开reset到这一个版本就可以了
6. git checkout -- <file> 将已经修改的文件(但是没有add)恢复到没有修改的状态
git push origin test:master         // 提交本地test分支作为远程的master分支 //好像只写这一句，远程的github就会自动创建一个test分支
git push origin tsy：master 就可以把issue5560推送到远程的master分支了


git push origin test:test              // 提交本地test分支作为远程的test分支


git checkout -b dev origin/dev
如果想删除远程的分支呢？类似于上面，如果:左边的分支为空，那么将删除:右边的远程的分支
git push <远程主机名> <本地分支名>:<远程分支名>
git pull <远程主机名> <远程分支名>:<本地分支名>
	git pull origin next:master
	如果远程分支是与当前分支合并，则冒号后面的部分可以省略
	git pull origin next
	如果当前分支与远程分支存在追踪关系，git pull就可以省略远程分支名:git branch --set-upstream master origin/next
	 git pull origin
	 如果当前分支只有一个追踪分支，连远程主机名都可以省略

'''