# encoding:utf-8
# 并发编程
# 如果想实现，其他线程先停止，再停止主线程

import threading
from threading import current_thread


# 创建一个MyThread类，继承Thread，并重写run方法
class MyThread(threading.Thread):
    def run(self):
        print(current_thread().getName(), 'start')
        print('run')
        print(current_thread().getName(), 'stop')


t1 = MyThread()
# 启动线程
t1.start()
# 
t1.join()

print(current_thread().getName(), 'end')
