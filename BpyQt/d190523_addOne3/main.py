# -*- coding: utf-8 -*-
# 主函数运行文件，平时不改动
# 这是仿照 C++的QT写的
from PyQt5 import QtCore, QtGui, QtWidgets
from addOne import addOne

if __name__ == "__main__":
    import sys
    a = QtWidgets.QApplication(sys.argv)
    w = addOne()
    w.show()
    sys.exit(a.exec_())
