import threading
import time

class myT(threading.Thread):
    def __init__(self,threadID,name,counter,delay):
        threading.Thread.__init__(self)
        self.threadID = threadID;
        self.name = name
        self.counter = counter
        self.delay = delay
    def run(self):
        print("开始线程")
        myPrint(self,self.counter,self.delay)
        print("退出线程")
        

def myPrint(threadName,counter,delay):
    for i in range(counter):
        print(threadName,i)
        time.sleep(delay)

th1 = myT(1,'th1',10,2)
th2 = myT(2,'th2',5,1)

th1.start()
th2.start()
th1.join()
th2.join()
print('退出主线程');
        
        
        
        
        
        