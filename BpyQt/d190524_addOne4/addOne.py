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

    
    
    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        self.count+=1
        self.label.setText(str(self.count))
        self.zShow.printf("count=%f", self.count)


if __name__ == "__main__":
    import sys
    a = QtWidgets.QApplication(sys.argv)
    w = addOne()
    w.show()
    
    sys.exit(a.exec_())
