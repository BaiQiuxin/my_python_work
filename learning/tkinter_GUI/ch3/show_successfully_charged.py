"""在tkinter窗口中显示充值成功后获得的道具"""

import tkinter
win = tkinter.Tk()
win.title("充值成功")
win.geometry("300x240")
window_str = "1.1级VIP30天\n\n2.每天额外赠送300金币7天\n\n3.全英雄限免30天\n"
tkinter.Label(win,text="充值成功！",font="Times 18 bold").pack()
tkinter.Label(win,text="\n恭喜获得：\n",font="16").pack(anchor="w",padx=45)
tkinter.Label(win,text=window_str,font="18",fg="red",justify="left").pack()
win.mainloop()