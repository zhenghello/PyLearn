 #!/usr/bin/python
# coding=UTF-8

import serial
import threading
import time

class mySerial(threading.Thread):
    uart=serial.Serial() #winsows系统使用com1口连接串行口
    revCount = 0
    
    def __init__(self,port,baudrate,timeout):
        threading.Thread.__init__(self)
        self.uart.port = port
        self.uart.baudrate = baudrate
        self.uart.timeout = timeout
        self.uart.open()

        
    def run(self):
        while 1:
            str = self.uart.readline()
            print(str)
            time.sleep(0.1)




# Serial的初始化Parameters:	
# port – Device name or None.
# baudrate (int) – Baud rate such as 9600 or 115200 etc.
# bytesize – Number of data bits. Possible values: FIVEBITS, SIXBITS, SEVENBITS, EIGHTBITS
# parity – Enable parity checking. Possible values: PARITY_NONE, PARITY_EVEN, PARITY_ODD PARITY_MARK, PARITY_SPACE
# stopbits – Number of stop bits. Possible values: STOPBITS_ONE, STOPBITS_ONE_POINT_FIVE, STOPBITS_TWO
# timeout (float) – Set a read timeout value.
# xonxoff (bool) – Enable software flow control.
# rtscts (bool) – Enable hardware (RTS/CTS) flow control.
# dsrdtr (bool) – Enable hardware (DSR/DTR) flow control.
# write_timeout (float) – Set a write timeout value.
# inter_byte_timeout (float) – Inter-character timeout, None to disable (default).
# Raises:	
# ValueError – Will be raised when parameter are out of range, e.g. baud rate, data bits.
# SerialException – In case the device can not be found or can not be configured.
#bytesize=EIGHTBITS, parity=PARITY_NONE, stopbits=STOPBITS_ONE

print("=======================begin=======================" )

port        = "COM8"    # 端口号
baudrate    = 115200    # 波特率
timeout     = 0.5       # 超时
myUart = mySerial(port,baudrate,timeout)
myUart.start()
myUart.join()   


print("=======================end=========================")