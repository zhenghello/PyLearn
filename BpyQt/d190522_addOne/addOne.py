# -*- coding: utf-8 -*-

"""
Module implementing addOne.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget

from Ui_addOne import Ui_Form


class addOne(QWidget, Ui_Form):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(addOne, self).__init__(parent)
        self.setupUi(self)
    
    __count = 0
    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        self.__count+=1
        # TODO: not implemented yet
        self.label.setText(str(self.__count))
        

if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    Form = addOne()
    Form.show()
    sys.exit(app.exec_())
