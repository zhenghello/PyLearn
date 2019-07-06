import json

class configFile():
    def __init__(self, path):
        self.path = path;
        try:
            with open(self.path, 'r') as f:
                self.dat = json.load(f);# 先读取json数据
            #print ("原始配置：", repr(self.dat)) #调试用
        except:
            self.dat ={};
            print("导入数据错误");
    def __del__(self):
        print('configFile del')
        
    def set(self, key, vlaue):
        self.dat[key] = vlaue;
        
    def get(self, key):
        try:
            value = self.dat[key];
        except:
            value = 0;
        return value;
        
    def save(self):
        try:
            with open(self.path, 'w') as f:
                json.dump(self.dat, f)
        except:
            print("路径错误！")
        
