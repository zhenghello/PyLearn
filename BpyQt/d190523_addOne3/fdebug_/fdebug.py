# -*- coding: utf-8 -*-

"""
Module implementing Fdebug.
郑凯鹏常用的显示窗体
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget

from Ui_fdebug import Ui_Fdebug

from PyQt5 import QtCore, QtGui, QtWidgets

class Fdebug(QWidget, Ui_Fdebug):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        构造函数
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Fdebug, self).__init__(parent)
        self.setupUi(self)
        self.show_count = 0;# 计算显示次数
    @pyqtSlot()
    def on_b_clear_clicked(self):
        """
        Slot documentation goes here.
        清空显示区域
        """
        self.show_count=0;  # 清空计数
        self.t_show.clear();# 清空显示
        
    def setText(self,str):
        """
        界面显示字符串
        """
        self.t_show.append("%d.%s"%(self.show_count, str))
        self.show_count+=1
    

if __name__ == "__main__":
    import sys
    a = QtWidgets.QApplication(sys.argv)
    w = Fdebug()
    w.show()
    
    w.setText("123456")
    
    sys.exit(a.exec_())
