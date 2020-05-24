# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 20:41:40 2019

@author: Aaron
"""

import tkinter as tk

def insert_point():
    var=entry.get()
    t.insert("insert",var)
def insert_end():
    var=entry.get()
    t.insert("end",var)

window=tk.Tk()
window.title("title")
window.geometry("300x300")

entry=tk.Entry(window,show="*")
entry.pack()

btn1=tk.Button(window,
               width=15,height=2,
               text="insert point",
               command=insert_point)
btn1.pack()

btn2=tk.Button(window,
               width=15,height=2,
               text="insert end",
               command=insert_end)
btn2.pack()

t=tk.Text(window,height=3)
t.pack()

window.mainloop()