# coding:utf-8

import Queue
import time
import random
import threading

queue = Queue.Queue()


class MyThread(threading.Thread):
    def __init__(self, queue, t, j):
        super(MyThread,self).__init__()
        self.queue = queue
        self.t = t
        self.j = j

    def run(self):
        time.sleep(self.j)
        self.queue.put(u'我是第%d个线程，我睡眠了%ds,当前时间是%s' % (self.t, self.j, time.ctime()))


count = 0
threads = []

for i in xrange(15):
    j = random.randint(1,8)
    threads.append(MyThread(queue, i, j))

for mt in threads:
    mt.start()

print "start time:", time.ctime()

while True:
    if not queue.empty():
        print queue.get()
        count += 1
    if count == 15:
        break