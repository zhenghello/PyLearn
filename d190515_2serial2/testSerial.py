 #!/usr/bin/python
# coding=UTF-8

import serial

print("serial in")

#try:

#bytesize=EIGHTBITS, parity=PARITY_NONE, stopbits=STOPBITS_ONE
ser=serial.Serial("COM5",115200,timeout=0.5) #winsows系统使用com1口连接串行口
if (ser.isOpen()):
    print("串口已经打开");
else:
    print("串口没有打开");
#ser.open()
print("串口详情参数：", ser)
ser.write('hello world!'.encode())#向端口写些数据
print(ser.name            )
print(ser.port            )
print(ser.baudrate        ) #波特率
print(ser.bytesize        ) #字节大小
print(ser.parity          ) #校验位N－无校验，E－偶校验，O－奇校验
print(ser.stopbits        ) #停止位
print(ser.timeout         ) #读超时设置
print(ser.writeTimeout    ) #写超时
print(ser.xonxoff         ) #软件流控
print(ser.rtscts          ) #硬件流控
print(ser.dsrdtr          ) #硬件流控
print(ser.interCharTimeout) #字符间隔超时
s = ser.read(10)            #从端口读10个字节
print("s = ",s)
ser.close()


print("serial over")