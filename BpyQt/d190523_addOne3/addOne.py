# -*- coding: utf-8 -*-

"""
Module implementing addOne.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget

from Ui_addOne import Ui_addOne

import sys
sys.path.append('./fdebug_')

import fdebug_.fdebug

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
        
        # 内部初始化
        zShow = fdebug();

    
    
    
    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        self.count+=1
        self.label.setText(str(self.count))
            



