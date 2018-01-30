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

	 
	 git merge --no-ff -m "merge with no-ff" dev
	 
'''
# 对于五层协议的理解
'''
一台计算机要和其他的计算机进行通信就需要连接到网络(不管是局域网还是跨网段)，计算机与计算机之间
通信遵循TCP/IP协议就可以实现互联。常用的协议模型为五层协议。从上到下为应用层、传输层、网络层
数据链路层和物理层。计算机A和计算机B进行通信，首先要知道计算机B的地址。那么在协议中规定，一个
唯一标识的程序有下面的几个元素：udp/tcp+port+IP。目的IP可以找到计算机B的网络地址，找到网络地址后
通过B的MAC地址直接将A的信息发送给B。但是B上运行着好多程序，那么那个程序才是要接受信息的程序。通过
port可以找到运行在B机器的程序。
可以将这个过程打一个比方，将送快递比喻网络间信息的传送。
比如公司现让我巴铁首都伊斯兰堡的一家烧饼店考察烧饼卖的好不好，首先我的知道伊斯兰堡在哪里(对方的IP)，之后我可能
先走十五里山路到乡里（路由）,之后我问乡长，去伊斯兰堡怎么走。乡长一脸崇拜的说，小伙子，虽然我不知道伊斯兰卡在
哪里，但是我建议你先到县城里去看看，问问县长。之后我就做公交车去去县城找县长（乡可以认为是MAC，
县可以认为是一个MAC地址）。县长说他也不知道，你要去伊斯兰卡，可以先到坐火车到北京，到北京之后再打听打听。
之后我就做火车去北京。下了火车，我就问工作人员，我怎么才可以到伊斯兰卡。工作人员告诉我可以做飞机
飞到伊斯兰卡。然后我到了伊斯兰卡。到了伊斯兰卡后我就可以在伊斯兰卡的飞机场的地图上找到烧饼店的位置
然后到烧饼店去考察下烧饼生意好不好做，我并没有去烧饼店吃烧饼。
对上述的场景进行的分析。
目的网络：伊斯兰卡
目的IP：烧饼店
目的端口：考察烧饼经营情况
源IP：某某地方的某某公司
源端口：烧饼经营
在这个信息传送的过程，我一直都知道目的地，没到一处地方，不管是做火车还是做飞机，其实是路由的方式不同
而已没在本质上都是MAC信息的传送。
'''

'''
网络编程注意事项
1. 网络传输的是byte格式，不能传输明文，故发送和接收之前都需要进行编码和解码
2. TCP传输是基于流的，传输需要解决粘包问题，如下所示minus
3. TCP是基于流的，所以需要加上报头和报头的长度部分(4bytes)，不然无法区分报头长度和数据长度
    也就是说，内容的完整发送需要包括三部分：报头长度，报头，数据
'''
while recv_size < data_size:
    minus = data_size - recv_size
    if minus > 1024:
        size = 1024
    else:
        size = minus
    recv_data = self.socket.recv(size)
    f.write(recv_data)
    recv_md5_obj.update(recv_data)
    recv_size += len(recv_data)
    self.process(recv_size, data_size