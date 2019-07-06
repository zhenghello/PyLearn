# -*- coding: utf-8 -*-

"""
Module implementing Fdebug.
郑凯鹏常用的显示窗体，
如何使用它：
创建一个对象后，常用的函数就三个，setTextStyle，setText，printf
"""

from PyQt5.QtCore    import pyqtSlot, Qt
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui     import QColor

import time  #时间模块

#import sys
#sys.path.append("../fdebug_/")
from Ui_fdebug import Ui_Fdebug


class Fdebug(QWidget, Ui_Fdebug):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None, hide_key=False):
        """
        构造函数
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Fdebug, self).__init__(parent)
        self.setupUi(self)
        # 内部自定义初始化操作 ---------------------------------------------------------------------begin
        #self.setWindowFlags(self.windowFlags()|Qt.Window); #设置为从类
        if(hide_key):
            self.b_clear.hide()
        print('Fdebug begin')    
    
    def __del__(self):             # 不触发它
        print('Fdebug __del__')  
    def closeEvent(self, event):   # 会触发它 
        print('Fdebug closeEvent')

    @pyqtSlot()
    def on_b_clear_clicked(self):
        """
        按键出发信号
        清空显示区域
        """
        self.t_show.clear();# 清空显示
        
    # 自定义函数---------------------------------------------------------------------begin
    def setTextStyle(self, str, bcol, fcol, fontW):
        """
        str：字符串内容
        bcol：背景色
        fcol：字体色
        fontW:字体宽度
        界面显示彩色的字符串
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
        界面显示字符串，会在前面叠加日期
        """
        self.t_show.append("%s%s"%(time.strftime("[%m-%d %H:%M:%S]", time.localtime()), str))
    def addText(self,str):
        """
        界面,在现有字符串后叠加字符串，不自动换行
        """
        str2=self.t_show.toPlainText()
        str2 += str;
        self.setText(str2)
    def printf(self, arg, *args):
        """
        界面显示print字符串，可以有多种格式
        """
        self.t_show.append(arg % args)
    def clear(self):
        """
        清除显示内容
        """
        self.t_show.clear();# 清空显示


# 调试自己的主函数代码---------------------------------------------------------------------begin
if __name__ == "__main__":
    import sys
    from PyQt5 import  QtWidgets
    a = QtWidgets.QApplication(sys.argv)
    w = Fdebug()
    w.show()
    w.setText("123456")
    w.setText("6789")
    w.addText("apple")
    w.setTextStyle("nihao", Qt.yellow, Qt.red, 12)
    
    print(Qt.yellow)
    print(Qt.red)
    w.printf("%d", 124)
    sys.exit(a.exec_())
