"""一个用Python实现GUI的简单尝试"""

from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title("这是一个ttk小demo")
style = Style()
style.configure("TButton", font=14, relief="flat", background="#00f5ff")
Button(text="这只是一个按钮", style="TButton").pack(pady=20)
root.mainloop()