#!/usr/bin/env python
import threading
import time

def run(n):
    semaphore.acquire()
    print('num:',n)
    time.sleep(3)
    semaphore.release()
    
semaphore = threading.BoundedSemaphore(5)
for i in range(22):
    t = threading.Thread(target=run,args=(i,))
    t.start()