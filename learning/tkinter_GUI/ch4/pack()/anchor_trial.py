"""通过anchor属性设置组件在父容器中的位置"""

import tkinter
win = tkinter.Tk()
tkinter.Label(win,text="下一步",bg="#8EBC90").pack(anchor="s",side="right",padx=10,pady=10)
win.mainloop()