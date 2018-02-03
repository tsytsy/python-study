'''
将线程声明为守护线程，必须在start() 方法调用之前设置，如果不设置为守护线程程序会被无限挂起。
当我们在程序运行中，执行一个主线程，如果主线程又创建一个子线程，主线程和子线程 就分兵两路，分别运行，那么当主线程完成
想退出时，会检验子线程是否完成。如果子线程未完成，则主线程会等待子线程完成后再退出。但是有时候我们需要的是只要主线程
完成了，不管子线程是否完成，都要和主线程一起退出，这时就可以 用setDaemon方法啦
守护线程有可能在主线程完成之前就执行完程序了.

打一个比方，非守护线程和主线程之间类似于亚当夏娃的关系，在程序中主线程可以产生一个子线程，子线程可以是守护线程
也可以是非守护线程。主线程和守护线程相当于孙悟空和猴毛的关系，孙悟空可以用猴毛变出好多孙悟空去干其他的事情。但是
一旦真身被完玩了，猴毛也就没了。而非守护线程和主线程之间的关系相当于亚当夏娃的关系，夏娃虽然是亚当用肋骨变得，但是
亚当死不死和夏娃其实没有半毛钱的关系的。
'''
import os
import threading
import time

def print_test(str1):
    print('print test', threading.enumerate(), os.getpid())
    time.sleep(5)
    print('from print test', str1)
    time.sleep(1)


def write(str1):
    print('print write', threading.enumerate(), os.getpid())

    time.sleep(1)
    print('from write', str1)
    time.sleep(1)

def count(n):
    print('thread %s' % n)
    time.sleep(3)
    print(threading.current_thread())


if __name__ == '__main__':
    # print('I am the main thread')
    # print(threading.enumerate())
    # print(os.getpid())
    # str1 = 'aaa'
    # t1 = threading.Thread(target=print_test, args=(str1,), name='lyt')
    # t2 = threading.Thread(target=write, args=(str1, ), name='tsy')
    # t1.setDaemon(True)
    # t1.start()
    # t2.start()
    # t1.join()
    # t2.join()
    thread_list = []
    start_time = time.time()
    for i in range(50):
        t = threading.Thread(target=count, args=(i, ))
        if i < 40:
            t.setDaemon(True)
        t.start()
        thread_list.append(t)
    # for t in thread_list:
    #     # print(i)
    #     t.join()

    # for t in thread_list[:40]:
    #     t.setDaemon(True)

    print(threading.enumerate())
    print('end')
    cost_time = time.time() - start_time
    print(cost_time)


