"""显示4以内的乘法表
grid()方法的使用
row表示行，column表示列
"""
import tkinter
win = tkinter.Tk()
win.title("tkinter的初使用")
"""
grid()方法的参数：
row         组件所在的行
column      组件所在的列
rowspan     组件横向合并的行数
columnspan  组件纵向合并的列数
sticky      组件填充所分配空间空白区域的方法
padx, pady  组件距离父容器边界的水平距离和垂直距离
"""
# grid(row=0,column=0,padx=10)设置组件位于第0行第0列，与其他组件的水平间距为10px
tkinter.Label(win,text="1*1=1",bg="#E0FFFF").grid(row=0,column=0,padx=10)
tkinter.Label(win,text="1*2=2",bg="#E0FFFF").grid(row=1,column=0,padx=10)
tkinter.Label(win,text="1*3=3",bg="#E0FFFF").grid(row=2,column=0,padx=10)
tkinter.Label(win,text="1*4=4",bg="#E0FFFF").grid(row=3,column=0,padx=10)
tkinter.Label(win,text="2*2=4",bg="#EEA9B8").grid(row=1,column=1,padx=10)
tkinter.Label(win,text="2*3=6",bg="#EEA9B8").grid(row=2,column=1,padx=10)
tkinter.Label(win,text="2*4=8",bg="#EEA9B8").grid(row=3,column=1,padx=10)
tkinter.Label(win,text="3*3=9",bg="#F08080").grid(row=2,column=2,padx=10)
tkinter.Label(win,text="3*4=12",bg="#F08080").grid(row=3,column=2,padx=10)
tkinter.Label(win,text="4*4=16",bg="#FFE1FF").grid(row=3,column=3,padx=10)
win.mainloop()