# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 07:56:49 2019

@author: Aaron
"""

import tkinter as tk
import tkinter.messagebox

def right():
    tkinter.messagebox.showinfo(title="成功",message="成功登入")
    
def wrong():
    #tkinter.messagebox.showinfo(title="錯誤",message="帳號或密碼有誤")
    tkinter.messagebox.askretrycancel(title="嗨你好",message="我帥嗎") 
def check():
    if account.get() != "user123" or password.get() != "password":
        wrong()
    else:
        right()


    
window=tk.Tk()
window.title("登入")


tk.Label(window,text="帳號",width=30).grid(row=0,column=0,pady=5)

account=tk.Entry(window,width=50)
account.grid(row=0,column=1)

tk.Label(window,text="密碼",width=30).grid(row=1,column=0,pady=5)

password=tk.Entry(window,width=50,show="*")
password.grid(row=1,column=1)

btn=tk.Button(window,width=80,text="登入",font=("Arial",14),command=check,bg="red",fg="white").grid(row=2,column=0,columnspan=2,padx=5,pady=10)


window.mainloop()