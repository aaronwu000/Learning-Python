# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 16:57:40 2019

@author: Aaron
"""

import tkinter as tk

def add():
    result.configure(text=str(int(num1.get())+int(num2.get())))


window=tk.Tk()
window.title("tk")
window.geometry("300x200")

lbl1=tk.Label(window,text="First Number")
lbl1.pack()
num1=tk.Entry(window)
num1.pack()
lbl2=tk.Label(window,text="Second Number")
lbl2.pack()
num2=tk.Entry(window)
num2.pack()
lbl3=tk.Label(window,text="Enter the Nunbers and click the button")
result = tk.Label(window,text="")
result.pack()
btn=tk.Button(window,text="add",command=add)
btn.pack()




window.mainloop()