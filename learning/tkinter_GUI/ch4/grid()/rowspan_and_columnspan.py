"""通过rowspan方法和columnspan方法合并行和列"""

import tkinter
win = tkinter.Tk()
tkinter.Label(win,text="columnspan=4",width=15,height=1,relief="groove",bg="#EDE19A").grid(row=0,column=0,columnspan=4)
tkinter.Label(win,text="columnspan=2",width=15,height=1,relief="groove",bg="#EDBE9A").grid(row=1,column=0,columnspan=2)
tkinter.Label(win,text="columnspan=2",width=15,height=1,relief="groove",bg="#EDBE9A").grid(row=1,column=2,columnspan=2)
tkinter.Label(win,width=15,height=1,relief="groove",bg="#E5AEAE").grid(row=2,column=0)
tkinter.Label(win,width=15,height=1,relief="groove",bg="#E5AEAE").grid(row=2,column=1)
tkinter.Label(win,width=15,height=1,relief="groove",bg="#E5AEAE").grid(row=2,column=2)
tkinter.Label(win,width=15,height=1,relief="groove",bg="#E5AEAE").grid(row=2,column=3)
win.mainloop()
