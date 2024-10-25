"""设置tkinter窗口文字的排列方式"""

import tkinter
"""
pack()方法参数：
side    设置组件水平展示或垂直展示，top(default)自上到下，bottom自下到上，left从左到右，right从右到左
padx    设置组件距离父容器的水平距离
pady    设置组件距离父容器的垂直距离
ipadx   设置组件内的文字距离组件边界的水平距离
ipady   设置组件内的文字距离组件边界的垂直距离
fill    设置组件填充所在的空白空间的方式，x完全填充水平方向，y完全填充垂直方向，both水平和垂直方向均完全填充，none(default)不填充
expand  设置组件是否完全填充其余空间
anchor  设置组件在父容器中的位置
before  设置组件应该位于指定组件的前面
after   设置组件应该位于制定组件的后面
"""
win = tkinter.Tk()
text1 = "暮冬时烤雪"
text2 = "迟夏写长信"
text3 = "早春不过一棵树"
# 在pack()方法中通过side参数设置排列方式为从左到右依次排列
tkinter.Label(win, text=text1, bg="#F5DFCC").pack(side="left")
tkinter.Label(win, text=text2, bg="#EDB584").pack(side="left")
tkinter.Label(win, text=text3, bg="#EF994C").pack(side="left")
win.mainloop()
"""
tkinter.Label(win, text=text1, bg="#F5DFCC").pack(side="bottom")
tkinter.Label(win, text=text2, bg="#EDB584").pack(side="bottom")
tkinter.Label(win, text=text3, bg="#EF994C").pack(side="bottom")

tkinter.Label(win, text=text1, bg="#F5DFCC").pack(side="bottom",padx=20,pady=5)
tkinter.Label(win, text=text2, bg="#EDB584").pack(side="bottom",padx=20,pady=5)
tkinter.Label(win, text=text3, bg="#EF994C").pack(side="bottom",padx=20,pady=5)

tkinter.Label(win, text=text1, bg="#F5DFCC").pack(side="bottom",padx=20,pady=5,ipadx=10,ipady=5)
tkinter.Label(win, text=text2, bg="#EDB584").pack(side="bottom",padx=20,pady=5,ipadx=10,ipady=5)
tkinter.Label(win, text=text3, bg="#EF994C").pack(side="bottom",padx=20,pady=5,ipadx=10,ipady=5)
"""