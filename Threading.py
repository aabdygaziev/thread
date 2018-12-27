import threading
import time
def clock(interval):
    i = 0
    while True:
        i += 1
        print(str(interval)+' '+str(i))
        time.sleep(interval)

t1 = threading.Thread(target=clock, args=(10,))
t1.start()

#t2 = threading.Thread(target=clock, args=(3,))
#t2.start()

#t3 = threading.Thread(target=clock, args=(1,))
#t3.start()

def countdown(count):
    i = 10
    while True:
        i -= 1
        print(str(count)+' '+str(i))
        time.sleep(count)
        if countdown()

t4 = threading.Thread(target=countdown, args=(1,))
t4.start()
