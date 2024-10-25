"""tkinter窗口中Widget组件的公共方法"""

import tkinter
win = tkinter.Tk()
label = tkinter.Label(win,text="上拜图灵只求服务可用\n\n下跪关公但求永不宕机\n\n风调码顺")
label.config(bg="#DEF1EF",fg="red",font=14)
label.pack()
win.mainloop()

"""
config(): 为组件配置参数。
keys(): 获取组件的所有参数，并返回一个列表。
"""
