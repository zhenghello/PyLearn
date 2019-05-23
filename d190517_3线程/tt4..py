import threading
import time

threads = []                #创建线程列表
thLock  = threading.Lock()  #创建一个线程锁

# 创建一个继承线程的类
class myT(threading.Thread):
    def __init__(self,threadID,name,counter,delay):
        threading.Thread.__init__(self)
        self.threadID = threadID;
        self.name = name
        self.counter = counter
        self.delay = delay
    def run(self):
        thLock.acquire() # 获取锁
        print("开始线程",self)
        myPrint(self,self.counter,self.delay)
        print("退出线程",self)
        thLock.release() # 释放锁
        
# 连续固定间隔打印内容
def myPrint(threadName,counter,delay):
    for i in range(counter):
        print(threadName,i)
        time.sleep(delay)

th1 = myT(1,'th1',10,0.5)
th2 = myT(2,'th2',5,1)

threads.append(th1)
threads.append(th2)

th1.start()
th2.start()
th1.join()
th2.join()

print('退出主线程');
        
        
        
        
        
        