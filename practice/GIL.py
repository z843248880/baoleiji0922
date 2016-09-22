#!/usr/bin/env python

import threading
import time

def run():
    global num
    lock.acquire()
    time.sleep(2)
    num += 1
    lock.release()
num = 0
lock = threading.Lock()
for i in range(1000):
    t = threading.Thread(target=run)
    t.start()
time.sleep(3)
print(num)