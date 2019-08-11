#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from tkinter import *

top = Tk()

Entry(top,width=50).grid(columnspan=4, column=0)

key = ['0', '1', '2', '3',
       '4', '5', '6', '7',
       '8', '9', '.', '=',
       '+', '-', 'x', '/']
for i in range(16):
    Button(top, text=key[i], width=10).grid(row=i // 4 + 1, column=i % 4)



top.mainloop()









