# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 18:31:18 2019

@author: Aaron
"""


import tkinter as tk


def convert():
    result.configure(text=str(int(degC.get())*5/9+32))
    

window=tk.Tk()
window.title("Temp Converter")
window.geometry("300x100")



tk.Label(window,text="deg C").place(x=50,y=0)
degC=tk.Entry(window)
degC.place(x=100,y=0)
tk.Label(window,text="deg F").place(x=50,y=25)
tk.Button(window,text="Convert",command=convert).place(x=120,y=50)
result = tk.Label(window,text="")
result.place(x=150,y=25)





window.mainloop()