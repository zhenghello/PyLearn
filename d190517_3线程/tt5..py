import threading
import time
import queue
import copy
threads     = []                #创建线程列表
thLock      = threading.Lock()  #创建一个线程锁

workQueue   = queue.Queue(20)   #创建一个队列
thList      = ['tx1','tx2','tx3','tx4','tx5','tx6','tx7','tx8','tx9','tx10']

# 创建一个继承线程的类
class myT(threading.Thread):
    def __init__(self,threadID,name,q,delay):
        threading.Thread.__init__(self)
        self.threadID = threadID;
        self.name = name
        self.qu = copy.copy(q)
        print("队列的ID=",id(self.qu))
        self.delay = delay
    def run(self):
        print("开始线程",self)
        myPrint(self,self.qu,self.delay)
        print("退出线程",self)
        
# 连续固定间隔打印内容
def myPrint(threadName,qq,delay):
    print("myPrintd的队列的ID=",id(qq))
    qe = copy.copy(qq)
    while not qe.empty():
        thLock.acquire() # 获取锁
        print(threadName,qe.get())
        thLock.release() # 释放锁
        time.sleep(delay)


#队列放入数据
for tName in thList:
    workQueue.put(tName) 
print("size=",workQueue.qsize())
w2   = queue.Queue(20)
w2 = copy.copy(workQueue);
print("size=",w2.qsize())
w2.get();
print("size2=",workQueue.qsize())
print("size2=",w2.qsize())


# 创建线程   
th1 = myT(1,'th1',workQueue,0.5)
th2 = myT(2,'th2',workQueue,1)

threads.append(th1)
threads.append(th2)

th1.start()
th2.start()
th1.join()
th2.join()

print('退出主线程');
        
        
        
        
        
        