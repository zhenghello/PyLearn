# -*- coding: utf-8 -*-

"""
Module implementing Fcom.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget

from Ui_fcom import Ui_Fcom

import serial

class Fcom(QWidget, Ui_Fcom):
    """
    串口窗体模块，
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Fcom, self).__init__(parent)
        self.setupUi(self)      #
        # 内部自定义初始化操作 ---------------------------------------------------------------------begin

        self.uart=serial.Serial() # type: serial.Serial

    @pyqtSlot()
    def on_pushButton_open_clicked(self):
        """
        打开和关闭串口

        # port            – Device name or None.
        # baudrate (int)  – Baud rate such as 9600 or 115200 etc.
        # bytesize        – Number of data bits. Possible values: FIVEBITS, SIXBITS, SEVENBITS, EIGHTBITS
        # parity          – Enable parity checking. Possible values: PARITY_NONE, PARITY_EVEN, PARITY_ODD PARITY_MARK, PARITY_SPACE
        # stopbits        – Number of stop bits. Possible values: STOPBITS_ONE, STOPBITS_ONE_POINT_FIVE, STOPBITS_TWO
        # timeout (float) – Set a read timeout value.
        """
        if (self.pushButton_open.text()=="打开"):
            # port            – Device name or None.
            # baudrate (int)  – Baud rate such as 9600 or 115200 etc.
            # bytesize        – Number of data bits. Possible values: FIVEBITS, SIXBITS, SEVENBITS, EIGHTBITS
            # parity          – Enable parity checking. Possible values: PARITY_NONE, PARITY_EVEN, PARITY_ODD PARITY_MARK, PARITY_SPACE
            # stopbits        – Number of stop bits. Possible values: STOPBITS_ONE, STOPBITS_ONE_POINT_FIVE, STOPBITS_TWO
            # timeout (float) – Set a read timeout value.
            self.uart.port = self.serial_PortName.currentText()                     # 端口号
            self.uart.baudrate = self.serial_PortName.currentText().toUint()        # 波特率
            self.uart.bytesize = self.serial_DataBits.currentText().toUInt()        # 数据位 5678
            self.uart.stopbits = self.serial_StopBits.currentText().toUInt()        # 停止位 1 和 2
            self.uart.parity   = self.serial_StopBits.currentText()                 # 校验位 N－无校验，E－偶校验，O－奇校验
            self.uart.timeout  = 0.1                                                # 超时时间
            self.uart.Open()
            self.pushButton_open.setText("关闭")
        else:
            self.pushButton_open.setText("打开")

    @pyqtSlot()
    def on_pushButton_com_num_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot()
    def on_pushButton_save_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot()
    def on_pushButton_send_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot()
    def on_pushButton_load_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot()
    def on_pushButton_clear_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError


# 调试自己的主函数代码---------------------------------------------------------------------begin
if __name__ == "__main__":
    from PyQt5 import QtWidgets
    import sys
    a = QtWidgets.QApplication(sys.argv)
    w = Fcom()
    w.show()
    sys.exit(a.exec_())
