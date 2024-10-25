"""为tkinter窗口添加标题"""

import tkinter
from tkinter import Label

win = tkinter.Tk()
win.title("tkinter的初级使用")
Label(win,text="\n\ngame over\n\n").pack()
win.mainloop()