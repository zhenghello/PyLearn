#！/use/bin/python3
class mydie:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        x = self.a
        self.a += 1  
        return x
        
myclass = mydie()
myite=iter(myclass)

print(next(myite))
print(next(myite))
print(next(myite))
print(next(myite))
print(next(myite))
    
    