# ttk更加美化
# 将tkinter写成Tkinter可兼容Python 2.x
# 被Variable类重新定向后，不可以再被操作

from tkinter import *
from tkinter import ttk


class App:
    def __init__(self, master):
        self.master = master
        self.init_widgets()

    def init_widgets(self):
        self.count = StringVar()
        show = Label(self.master, width=30, background='white', font=('times', 20), textvariable=self.count)
        show.pack()
        bn = ttk.Button(self.master, text='单击我')
        bn.pack(fill=BOTH, expand=YES)
        # 为左键单击事件绑定处理方法
        bn.bind('<Button-1>', self.one)

    def one(self, event):
        try:
            my_num = int(self.count.get())
        except :
            my_num = 0
        my_num = my_num + 1
        self.count.set(my_num)


root = Tk()
root.title('简单绑定')
App(root)
root.mainloop()
