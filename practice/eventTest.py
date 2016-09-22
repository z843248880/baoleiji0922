#!/usr/bin/env python

import threading
import time
def lighter():
    count = 0
    event.set()
    while True:
        if count >= 3 and count <= 5:
            event.clear()
            time.sleep(1)
            print('now is red,please waiting.')
        elif count > 5:
            event.set()
            time.sleep(1)
            print('now is green,you can go.')
            count = 0
        else:
            time.sleep(1)
            print('now is green,you can go.')
        count +=1 
        time.sleep(1)
def car(carname):
    while True:
        if event.is_set():
            print('gogogo.')
            time.sleep(1)
        else:
            print('nonono.')
            event.wait()
            
event = threading.Event()
l1 = threading.Thread(target=lighter)
l1.start()
c1 = threading.Thread(target=car,args=('tesla',))
c1.start()