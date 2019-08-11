#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from tkinter import *
top = Tk()

fm1 = Frame(top)
fm1.pack(side=LEFT, fill=BOTH, expand=YES)
Button(fm1, text='button1').pack(side=TOP, fill=X, expand=YES)
Button(fm1, text='button2').pack(side=TOP, fill=X, expand=YES)
Button(fm1, text='button3').pack(side=TOP, fill=X, expand=YES)

fm2 = Frame(top)
fm2.pack(side=LEFT, expand=YES)
Button(fm2, text='button21').pack(side=LEFT, fill=Y, expand=YES)
Button(fm2, text='button22').pack(side=LEFT, fill=Y, expand=YES)
Button(fm2, text='button23').pack(side=LEFT, fill=Y, expand=YES)

fm3 = Frame(top)
fm3.pack(side=RIGHT, fill =BOTH, expand=YES)
Button(fm3, text='button31').pack(side=TOP, fill=Y, expand=YES)
Button(fm3, text='button32').pack(side=TOP, fill=Y, expand=YES)
Button(fm3, text='button33').pack(side=TOP, fill=Y, expand=YES)

top.mainloop()









