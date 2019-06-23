# -*- coding: utf-8 -*-

"""
Module implementing Fdebug.
郑凯鹏常用的显示窗体
"""

from PyQt5.QtCore   import pyqtSlot, Qt
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QColor


#import sys
#sys.path.append("../fdebug_/")
from Ui_fdebug import Ui_Fdebug


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
        # 内部自定义初始化操作 ---------------------------------------------------------------------begin
        self.setWindowFlags(self.windowFlags()|Qt.Window); #设置为从类
        self.show_count = 0;# 计算显示次数
        
    @pyqtSlot()
    def on_b_clear_clicked(self):
        """
        Slot documentation goes here.
        清空显示区域
        """
        self.show_count=0;  # 清空计数
        self.t_show.clear();# 清空显示
        
    # 自定义函数---------------------------------------------------------------------begin
    def setTextStyle(self, str, bcol, fcol, fontW):
        """
        界面显示字符串
        """
        if(str is None):return;# 忽略空白内容
        self.t_show.setTextBackgroundColor(bcol);
        self.t_show.setTextColor(fcol);
        self.t_show.setFontPointSize(fontW);
        self.t_show.append (str);#这个指定用来显示调试信息的文本框
        self.t_show.setTextBackgroundColor(QColor(255,255,255));
        self.t_show.setTextColor(QColor(0,0,0));
        self.t_show.setFontPointSize(8);
        
    def setText(self,str):
        """
        界面显示字符串
        """
        self.t_show.append("%d.%s"%(self.show_count, str))
        self.show_count+=1
        
    def printf(self, arg, *args):
        """
        界面显示print字符串
        """
        self.t_show.append(arg % args)
        
# 调试自己的主函数代码---------------------------------------------------------------------begin
if __name__ == "__main__":
    import sys
    from PyQt5 import  QtWidgets
    a = QtWidgets.QApplication(sys.argv)
    w = Fdebug()
    w.show()
    w.setText("123456")
    w.setTextStyle("nihao", Qt.yellow, Qt.red, 12)
    
    print(Qt.yellow)
    print(Qt.red)
    w.printf("%d", 124)
    sys.exit(a.exec_())
