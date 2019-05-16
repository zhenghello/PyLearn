class myC:
    def __init__(self,arg1,arg2):
        self.a1=arg1;
        self.a2=arg2;
    def putMsg(self):
        print("this is myC!","a1=",self.a1,"a2=",self.a2);
        
        
        
print("=======================begin=======================" )
a = myC(123,456)
a.putMsg();
print("=======================end=========================")