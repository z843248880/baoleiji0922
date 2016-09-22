#!/usr/bin/env python


import threading
import time
def run(t):
    print('t:',t)
    time.sleep(2)
    print('1111111111111111111')
for i in range(3):
    t = threading.Thread(target=run,args=("t-%s" % i,))
    t.setDaemon(True)
    t.start()

# t1 = threading.Thread(target=run,args=("t1",))
# t2 = threading.Thread(target=run,args=("t2",))
# t1.start()
# t1.join()
# t2.start()
# print('thread done.')  

 
# 
# 
# run('t1')
# run('t2')