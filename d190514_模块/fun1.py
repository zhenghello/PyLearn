import sys
def printPath():
    for x in sys.path:
        print(x)
    return
    
if __name__ == "__main__":
    print("I am main");
else:
    print("I am fun");
    
