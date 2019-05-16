class myC:
    def __init__(self,arg1,arg2):
        print("myC is Create!")
        self.a1=arg1;
        self.a2=arg2;
    def putMsg(self):
        print(self);
        print(self.__class__)
        
        
        
        
print("=======================begin=======================" )
a = myC(123,456)
a.putMsg();
b = myC(789,101)
b.putMsg();
c = myC(123,456)
c.putMsg();
d = myC(789,101)
d.putMsg();
print("=======================end=========================")