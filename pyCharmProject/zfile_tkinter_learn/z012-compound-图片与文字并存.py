from tkinter import *
# 导入ttk
from tkinter import ttk


class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()

    def initWidgets(self):
        # 创建一个位图
        bm = PhotoImage(file='z012serial.png')
        # 创建一个Label，同时指定text和image
        self.label = ttk.Label(
            self.master,
            text='学编程\n神器',
            image=bm,
            font=('StSong', 20, 'bold'),
            foreground='red'
            )
        self.label.bm = bm
        # 设置Label默认的compound为None
        self.label['compound'] = None
        self.label.pack()
        # 创建Frame容器，用于装多个Radiobutton
        f = ttk.Frame(self.master)
        f.pack(fill=BOTH, expand=YES)
        compounds = ('None', "LEFT", "RIGHT", "TOP", "BOTTOM", "CENTER")
        # 定义一个StringVar变量，用作绑定Radiobutton的变量
        self.var = StringVar()
        self.var.set('None')
        # 使用循环创建多个 Radion button组件
        for val in compounds:
            Radiobutton(
                f,
                text=val,
                padx=20,
                variable=self.var,
                command=self.change_compound,
                value=val
                        ).pack(side=LEFT, anchor=CENTER)

    # 都是同一个var，是如何实现读取到被选中的那个的呢？
    # 实现change_compound方法，用于动态改变Label的compound选项
    def change_compound(self):
        self.label['compound'] = self.var.get().lower()
        print(self.var.get())

root = Tk()
root.title("compound测试")
App(root)
root.mainloop()
