# Python 3.x使用这行
from tkinter import *


class App:
    def __init__(self, master):
        self.master = master
        self.count = 0
        self.show = Label(self.master, text=str(self.count), height=10)
        self.show.pack()
        self.button = Button(self.master, text="按下加一", command=self.button_add())
        self.button.pack()

    def button_add(self):
        self.count = self.count+1
        self.show['text'] = str(self.count)


root = Tk()
root.title("数字加一")
App(root)
root.mainloop()
