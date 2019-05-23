def listM(x):
    show = [0]
    for i in range(1,x+1):
        show.clear()
        for j in range(1,i+1):
            t = [j]
            show += t
        print(show)
        
def listM2(x):
    num1=1
    num2=2
    show=["12","34"]
    print
    for i in range(1,x+1):
        show.clear()
        for j in range(1,i+1):
            st = "%2d"%(i)+" X "+"%2d"%(j)+" = "+"%3d"%(i*j)
            show.append(st)
        print(show)

listM(10);

listM2(15);
         
        