#!/usr/bin/env python

import time
import threading
import queue

q = queue.Queue(maxsize=10)

def producer():
    count = 0
    while True:
        q.put("bone")
        print('produce a bone : %s' % count)
        count += 1
        time.sleep(1)
def consumer(name):
    while True:
        q.get()
        print('%s eat a bone.' % name)
        time.sleep(1)
p1 = threading.Thread(target=producer)
p1.start()
c1 = threading.Thread(target=consumer,args=('zsc',))
c2 = threading.Thread(target=consumer,args=('ZSC',))
c1.start()
c2.start()