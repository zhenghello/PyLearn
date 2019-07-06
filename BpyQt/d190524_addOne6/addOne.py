# -*- coding: utf-8 -*-

"""
Module implementing addOne.
"""

#from PyQt5.QtCore import QCoreApplication

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget
from PyQt5 import  QtWidgets



from Ui_addOne import Ui_addOne

# 导入模块路径 --------------------------------------------begin
import main_path
main_path.path_append();  #导入路径


from fdebug import  Fdebug
from jsonConfig import configFile
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
        self.__dat_config_load();  #导入配置
    
    def closeEvent(self, event):
        self.__dat_config_save();  #保存配置

    
    
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
        
    @pyqtSlot()
    def on_pushButton_end_clicked(self):
        print("关闭自己")
        self.__dat_config_save();  #保存配置
        self.close();
    # ************************** 内部函数 **************************
    def __dat_config_save(self):
        """
        @函数功能：保存配置模块
        """
        cfg = configFile('./zConfig/AllConfig.json');
        # 开始写入要保存的数据
        cfg.set('lineEdit.text', self.lineEdit.text())
        cfg.save()

    def __dat_config_load(self):
        """
        @函数功能：导入配置模块
        """
        cfg = configFile('./zConfig/AllConfig.json');
        # 开始读取要导入的数据
        self.lineEdit.setText(cfg.get('lineEdit.text'))

# ******************************************* 模块结束 ******************************************* #



if __name__ == "__main__":
    import sys
    a = QtWidgets.QApplication(sys.argv)
    w = addOne()
    w.show()
    
    sys.exit(a.exec_())
