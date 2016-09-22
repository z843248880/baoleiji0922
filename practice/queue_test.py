#!/usr/bin/env python

import queue

q = queue.PriorityQueue()
q.put((-1,'zrx'))
q.put((13,'aqq'))
q.put((9,'zsc'))
print(q.get())
print(q.get())
print(q.get())




# q = queue.Queue(maxsize=3)
# q.put(1)
# q.put(2)
# q.put_nowait(3)
# 
# print(q.get())
# print(q.get())
# print(q.get_nowait())
