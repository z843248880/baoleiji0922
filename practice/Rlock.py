import threading,time
 
def run1():
    print("grab the first part data")
    lock.acquire()
    global num
    num +=1
    lock.release()
    return num
def run3():
    lock.acquire()
    res = run1()
    print('--------brun1-----')
    lock.release() 
 
if __name__ == '__main__':
 
    num = 0
    lock = threading.Lock()
    for i in range(10):
        t = threading.Thread(target=run3)
        t.start()
 
while threading.active_count() != 1:
    print(threading.active_count())
else:
    print('----all threads done---')
    print(num)