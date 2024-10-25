"""指定tkinter窗口的大小及文字的样式"""

import  tkinter

win = tkinter.Tk()
win.geometry("300x200")

# foreground(fg)和background(bg)组件
tkinter.Label(win,text="小扣柴扉久不开",fg="red",bg="#C3DEEF").pack()

# width和height组件
# tkinter.Label(win,text="小扣柴扉久不开",fg="red",bg="#C3DEEF",width=20,height=3).pack()
# 设置高度时，大部分组件单位为px，部分如Label，以行为单位

# anchor用于设置文字在组件内的位置，默认center，水平垂直均居中
# tkinter.Label(win,text="小扣柴扉久不开",fg="red",bg="#C3DEEF",width=20,height=3,anchor="nw").pack()
# anchor属性可以用“nw”也可以用tkinter.NW

# padx和pady用于设置组件间的间距
# tkinter.Label(win,text="小扣柴扉久不开",fg="red",bg="#C3DEEF",padx=20,pady=10).pack()
# 单位为px

# font用于设置文件属性
# tkinter.Label(win,text="小扣柴扉久不开",fg="red",bg="#C3DEEF",font="华文新魏 16 bold").pack()
# 参数有：size字号，单位px；family字体，如times；weight粗细，如bold；slant斜体，如italic；underline添加下划线，True/False；overstrike添加删除线，True/Flase

# relief用于设置组件的边框属性
# tkinter.Label(win,text="小扣柴扉久不开",fg="red",bg="#C3DEEF"，relief="solid).pack()
# 有solid, raised, sunken, flat, groove, ridge六种属性值

# cursor设置当鼠标指针悬停在组件上时的指针样式
# tkinter.Label(win,text="小扣柴扉久不开",fg="red",bg="#C3DEEF"，cursor="spide, relief="groove").pack(padx=5,pady=5,side=tkinter.LEFT)

win.mainloop()