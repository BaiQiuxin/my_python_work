"""这是一个用Python实现GUI的简单尝试"""
import tkinter

win = tkinter.Tk()
win.title("这是一个ttk小demo")
# 添加按钮组件，然后设置样式，text：按钮上的文字；font：设置字号；relief：设置边框样式；
# bg：设置背景色；pack：包装按钮，目的是让按钮显示在窗口中
tkinter.Button(win, text="这只是一个按钮", font=14, relief="flat", bg="#00f5ff").pack(pady=20)
win.mainloop()