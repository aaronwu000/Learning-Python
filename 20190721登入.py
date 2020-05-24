# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 19:10:31 2019

@author: Aaron
"""

import tkinter as tk
import tkinter.font as tkf
import tkinter.messagebox

from PIL import Image,ImageTk

def login():
    if account.get()=="admin" and password.get()=="123":
        tkinter.messagebox.showinfo("訊息","登入成功")
    else:
        tkinter.messagebox.askretrycancel("訊息","登入失敗，是否重試")
        =
window=tk.Tk()
window.title("使用者登入")
window.geometry("500x300")


image_file=ImageTk.PhotoImage(image=Image.open("mario.png"))
print(image_file)
lbl=tk.Label(window,image=image_file)
lbl.place(x=0,y=0)


tk.Label(window,text="帳號:",font=tkf.Font(family="微軟正黑體",size=18)).place(x=75,y=130)
account=tk.Entry(window,font=tkf.Font(family="微軟正黑體",size=18))
account.place(x=145,y=130)
tk.Label(window,text="密碼:",font=tkf.Font(family="微軟正黑體",size=18)).place(x=75,y=180)
password=tk.Entry(window,font=tkf.Font(family="微軟正黑體",size=18),show="*")
password.place(x=145,y=180)
tk.Button(window,text="Sign up",font=tkf.Font(family="微軟正黑體",size=18),bg="red",fg="black",command=login).place(x=75,y=230,width=160,height=50)
tk.Button(window,text="Login",font=tkf.Font(family="微軟正黑體",size=18),bg="green",fg="black",command=login).place(x=270,y=230,width=160,height=50)




window.mainloop()