"""设置tkinter窗口的样式"""

import tkinter
win = tkinter.Tk()
win.title("tkinter的初级使用")
win.geometry("300x150")
win.configure(bg="yellow")
win.maxsize(500,500)
couple = "\n\n上联：足不出户一台电脑打天下\n\n下联：窝宅在家一双巧手定乾坤\n\n横批：量我风采"
tkinter.Label(win,text=couple,bg="yellow").pack()
win.mainloop()