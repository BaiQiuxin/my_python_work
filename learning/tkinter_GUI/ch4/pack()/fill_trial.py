"""使用fill方法填充tkinter窗口"""

import tkinter
win = tkinter.Tk()
txt = "枯藤老树昏鸦，小桥流水人家。"
tkinter.Label(win,text=txt,bg="#E6F5C8",fg="red",font="14").pack(side="left",fill="y")
win.mainloop()