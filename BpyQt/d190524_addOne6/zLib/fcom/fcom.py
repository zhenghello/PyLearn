# -*- coding: utf-8 -*-

"""
Module implementing Fcom.
"""
# 导入模块路径 --------------------------------------------后期删除
if __name__ == "__main__":
    import os
    #子模块要倒退两个文件夹
    path = os.path.abspath('../..')  # 表示当前所处的文件夹上一级文件夹的绝对路径
    #修改当前工作目录
    os.chdir(path)
    import main_path
    main_path.path_append();  #导入路径



from PyQt5.QtCore    import pyqtSlot, Qt
from PyQt5.QtWidgets import QWidget
from Ui_fcom import Ui_Fcom

# 调用的模块
from fdebug import  Fdebug          # 用于显示模块
from jsonConfig import configFile   # 用于保存配置模块

import serial                     #串口模块
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
        #self.setWindowFlags(self.windowFlags()|Qt.Window); #设置为从类
        self.uart=serial.Serial() # 串口对象创建
        self.myshow=Fdebug(self, hide_key=True)  # 创建显示对象模块fdebug,并且隐藏按键
        self.verticalLayout_main.insertWidget(0, self.myshow) #模块放到框体内
        self.myshow.show()
        self.myshow.clear()
        self.myshow.printf("串口模块")
        self.__dat_config_load();  #导入配置
    
    def closeEvent(self, event):
        self.__dat_config_save();  #保存配置
        
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

    # ************************** 内部函数 **************************
    def __dat_config_save(self):
        """
        @函数功能：保存配置模块
        """
        cfg = configFile('./zConfig/AllConfig.json');
        # 开始写入要保存的数据
        cfg.set('serial_BaudRate.currentIndex'    , self.serial_BaudRate.currentIndex())
        cfg.set('serial_DataBits.currentIndex'    , self.serial_DataBits.currentIndex())
        cfg.set('serial_StopBits.currentIndex'    , self.serial_StopBits.currentIndex())
        cfg.set('serial_Parity.currentIndex'      , self.serial_Parity.currentIndex())
        cfg.set('serial_send.text'                , self.serial_send.text())
        
        cfg.set('check_hex_send.isChecked'          , self.check_hex_send.isChecked())
        cfg.set('check_new_line.isChecked'          , self.check_new_line.isChecked())
        cfg.set('check_show_hex.isChecked'          , self.check_show_hex.isChecked())
        cfg.set('check_hide.isChecked'              , self.check_hide.isChecked())

        cfg.save()

    def __dat_config_load(self):
        """
        @函数功能：导入配置模块
        """
        cfg = configFile('./zConfig/AllConfig.json');
        # 开始读取要导入的数据
        self.serial_BaudRate.setCurrentIndex(cfg.get('serial_BaudRate.currentIndex', 0))
        self.serial_DataBits.setCurrentIndex(cfg.get('serial_DataBits.currentIndex', 0))
        self.serial_StopBits.setCurrentIndex(cfg.get('serial_StopBits.currentIndex', 0))
        self.serial_Parity.setCurrentIndex(cfg.get('serial_Parity.currentIndex', 0))
        self.serial_send.setText(cfg.get('serial_send.text', '*'))

        self.check_hex_send.setChecked(cfg.get('check_hex_send.isChecked', False))
        self.check_new_line.setChecked(cfg.get('check_new_line.isChecked', False))
        self.check_show_hex.setChecked(cfg.get('check_show_hex.isChecked', False))
        self.check_hide.setChecked(cfg.get('check_hide.isChecked', False))




        
# 调试自己的主函数代码---------------------------------------------------------------------begin
if __name__ == "__main__":

    
    from PyQt5 import QtWidgets
    import sys
    a = QtWidgets.QApplication(sys.argv)
    w = Fcom()
    w.show()
    sys.exit(a.exec_())
