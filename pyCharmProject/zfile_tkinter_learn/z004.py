#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from tkinter import *
top = Tk()

top.title("窗口标题")
w = Label(top,text="hello tkinter!")
w.pack()

b = Button(top, activebackground = '#ff4400',text = "按键")
b.pack()

top.mainloop()









