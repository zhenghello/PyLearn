# -*- coding: utf-8 -*-

"""
Module implementing addOne.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget
from PyQt5 import  QtWidgets



from Ui_addOne import Ui_addOne

# 导入模块路径 --------------------------------------------begin
import sys
import json
sys.path.append('./zLib/fdebug') 

from fdebug import  Fdebug

class addOne(QWidget, Ui_addOne):
    """
    Class documentation goes here.
    """
    count = 0
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(addOne, self).__init__(parent)
        self.setupUi(self)
        
        # 内部自定义初始化操作 ---------------------------------------------------------------------begin
        self.zShow = Fdebug(self);
        self.zShow.show();
        self.verticalLayout.insertWidget(0, self.zShow)
        
    def __del__(self):
        print("del");


    
    
    @pyqtSlot()
    def on_pushButton1_clicked(self):
        """
        Slot documentation goes here.
        """
        self.count+=1
        self.zShow.printf("count=%f", self.count)
        
    @pyqtSlot()
    def on_pushButton2_clicked(self):
        """
        Slot documentation goes here.
        """
        self.count+=1
        self.zShow.printf("count=%f", self.count);
        
        data = {
                'no' : 1,
                'name' : 'Runoob',
                'url' : 'http://www.runoob.com'
                }
 
        json_str = json.dumps(data)
        print ("Python 原始数据：", repr(data))
        print ("JSON 对象：", json_str)
        data['name'] = self.lineEdit.text()
        # 写入json
        with open('./zConfig/AllConfig.json', 'w') as f:
            json.dump(data, f)
        
        # 读取数据
        with open('./zConfig/AllConfig.json', 'r') as f:
            data = json.load(f)
        print ("读取数据：", repr(data))
        
        
    @pyqtSlot()
    def on_pushButton3_clicked(self):
        self.__dat_config_load();
        
    @pyqtSlot()
    def on_pushButton4_clicked(self):
        self.__dat_config_save();
    
    
    
    
    # ************************** 内部函数 **************************
    def __dat_config_save(self):
        """
        @函数功能：保存配置模块
        @输入参数：无
        @输出参数：无 
        """
        try:
            with open('./zConfig/AllConfig.json', 'r') as f:
                dat = json.load(f)# 先读取json数据
        except:
            print("导入数据错误")
        
        # *** 要保存的数据在这里操作 *** begin   
        
        dat['lineEdit_text']=self.lineEdit.text();
        
        # *** 要保存的数据在这里操作 *** end
        
        
        with open('./zConfig/AllConfig.json', 'w') as f:
            json.dump(dat, f)# 再写入json数据
        
    def __dat_config_load(self):
        """
        @函数功能：导入配置模块
        @输入参数：无
        @输出参数：无 
        """
        try:
            with open('./zConfig/AllConfig.json', 'r') as f:
                dat = json.load(f)# 先读取json数据
            # *** 要导出的数据在这里操作 *** begin   
            
            self.lineEdit.setText(dat['lineEdit_text']);
            
            # *** 要导出的数据在这里操作 *** end
        except:
            print("导入数据错误")
# ******************************************* 模块结束 ******************************************* #



if __name__ == "__main__":
    import sys
    a = QtWidgets.QApplication(sys.argv)
    w = addOne()
    w.show()
    
    sys.exit(a.exec_())
