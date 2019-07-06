# -*- coding: utf-8 -*-

"""
Module implementing Fcom.
"""

from PyQt5.QtCore    import pyqtSlot, Qt
from PyQt5.QtWidgets import QWidget

from Ui_fcom import Ui_Fcom


# 导入模块路径 --------------------------------------------begin
import sys
sys.path.append('../fdebug') 

from fdebug import  Fdebug        # 用于显示模块
import serial
import serial.tools.list_ports    #当前串口列表



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
        self.uart=serial.Serial() # 串口对象创建
        self.myshow=Fdebug(self, hide_key=True)  # 创建显示对象模块fdebug,并且隐藏按键
        self.verticalLayout_main.insertWidget(0, self.myshow) #模块放到框体内
        self.myshow.show()
        self.myshow.clear()
        self.myshow.printf("串口模块")
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
            self.uart.port = self.serial_PortName.currentText()                # 端口号
            self.uart.baudrate = int(self.serial_BaudRate.currentText())       # 波特率
            self.uart.bytesize = int(self.serial_DataBits.currentText())       # 数据位 5678
            self.uart.stopbits = int(self.serial_StopBits.currentText())       # 停止位 1 和 2
            self.uart.parity   = self.serial_Parity.currentText()              # 校验位 N－无校验，E－偶校验，O－奇校验
            self.uart.timeout  = 0.1                                           # 超时时间
            try:
                self.uart.open()
                self.pushButton_open.setText("关闭")
                self.myshow.setTextStyle("打开串口成功", Qt.white, Qt.green, 12)

            except:
                #打开串口失败的操作
                self.uart.close()
                self.myshow.setTextStyle("打开串口失败", Qt.white, Qt.red, 12)
        else:
            self.uart.close()
            self.pushButton_open.setText("打开")
            self.myshow.setTextStyle("关闭串口", Qt.white, Qt.red, 12)


    @pyqtSlot()
    def on_pushButton_com_num_clicked(self):
        """
        按下会选出当前可用的串口号
        """
        port_list = list(serial.tools.list_ports.comports()) #列出当前可用串口号
        self.serial_PortName.clear();
        for com in port_list:
            com_name =list(com)
            self.serial_PortName.addItem(com_name[0])
            
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
