class myC:
    def __init__(this,arg1,arg2):#构造函数
        print("myC is Create!")
        this.a1=arg1;
        this.a2=arg2;
    def __del__(this):          #析构函数
        print("myc is Delete")
    def __call__(this):         #对象被直接调用时的函数
        print("myC is Call")
    def __repr__(this):
        print("myC is Printing")#对象被打印
    def putMsg(this):
        print(this);
        print(this.__class__)
        
        
        
        
print("=======================begin=======================" )
a = myC(123,456)
a.putMsg();
a();
print(a)


b = myC(789,101)
b.putMsg();




print("=======================end=========================")

