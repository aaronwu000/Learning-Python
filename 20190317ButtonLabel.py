# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 19:17:57 2019

@author: Aaron
"""

import tkinter as tk
import tkinter.messagebox
def clickMe():
    tkinter.messagebox.showinfo(title="hi",message="衝啥啦")
on_hit=False
def toggle():
    global on_hit
    if on_hit:
        var.set("")
        on_hit=False
    else:
        var.set("-_-")
        on_hit=True
window=tk.Tk()
window.title("我的GUI")
window.geometry("300x300")
var=tk.StringVar()
l=tk.Label(window,
           textvariable=var,
           font=("Arial",12),
           width=15,height=2,
           bg="#A9D",fg="#F84")
l.pack()
"""
e=tk.Entry(window,width=20)
e.pack()
"""
btn1=tk.Button(window,
               text="???",
               width=20,
               bg="#89E",fg="#7F3",
               command=clickMe)
btn1.pack()
btn2=tk.Button(window,
               text="切換開關",
               width=20,
               command=toggle)
btn2.pack()
window.mainloop()