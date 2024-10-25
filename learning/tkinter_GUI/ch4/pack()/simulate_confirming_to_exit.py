"""模拟确认退出本窗口的对话框"""

import tkinter
win = tkinter.Tk()
win.geometry("350x150")
win.title("tkinter的初使用")
txt1 = tkinter.Label(win,text="确定退出本窗口吗？")
txt2 = tkinter.Label(win,text="果断退出",bg="#c1ffc1")
txt3 = tkinter.Label(win,text="我再想想",bg="#cdb5cd")
txt1.pack(fill="x",pady=20) # fill='x'设置组件始终水平居中表示
# side和anchor组合实现组件在窗口右下角显示
txt2.pack(side='right',padx='10',ipadx='6',pady='20',anchor='se')
txt3.pack(side='right',padx='10',ipadx='6',pady='20',anchor='se')
win.mainloop()