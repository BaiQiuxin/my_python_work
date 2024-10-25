"""设置tkinter窗口的大小及位置"""

import tkinter
win = tkinter.Tk()
win.title("tkinter的窗口及位置")           # 窗口的标题
win.configure(bg="#a7ea90")             # 窗口的背景色
winw = 300                              # 窗口的宽度
winh = 220                              # 窗口的高度
srch = win.winfo_screenheight()         # 获取屏幕高度
srcw = win.winfo_screenwidth()          # 获取屏幕宽度
x = int((srcw - winw)/2)    #计算窗口的水平位置，取整
y = int((srch - winh)/2)    #计算窗口的垂直位置，取整
win.geometry(f"{winw}x{winh}+{x}+{y}")  # 设置窗口大小及位置
window_str = "\n\n程序员鄙视链\n\n一等码农搞算法，吃香喝辣调调参\n\n二等码农搞架构，高并低延能吹牛\n\n三等码农搞工程，怼天怼地怼PM\n\n四等码农搞前端，浮层像素老黄牛"
tkinter.Label(win,text=window_str,bg="#a7ea90").pack()
win.mainloop()