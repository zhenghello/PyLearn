# -*- coding: utf-8 -*-
# 主函数运行文件，平时不改动
# 这是仿照 C++的QT写的
from PyQt5 import QtWidgets

if __name__ == "__main__":
    
    import main_path
    main_path.path_append();  #导入路径
    
    import sys
    from addOne import addOne
    a = QtWidgets.QApplication(sys.argv)
    w = addOne()
    w.show()
    sys.exit(a.exec_())
