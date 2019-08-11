#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from tkinter import *
top = Tk()
li = ['C', 'python', 'php', 'html', 'SQL', 'java']
movie = ['CSS', 'jQuery', 'Bootstrap']
listb1 = Listbox(top)
listb2 = Listbox(top)
for item in li:
    listb1.insert(0, item)
for item in movie:
    listb2.insert(0, item)
listb1.pack()
listb2.pack()
top.mainloop()









