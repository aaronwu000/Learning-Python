# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 20:12:37 2019

@author: Aaron
"""

import tkinter as tk

window=tk.Tk()
window.title("登入")
window.geometry("600x300")

colours=["red","orange","yellow","green","blue","cyan","purple"]

r=0
for c in colours:
    tk.Label(window,text=c,width=15,relief="ridge").grid(row=r,column=0)
    tk.Entry(window,bg=c,width=15,relief="sunken").grid(row=r,column=1)
    r+=1
window.mainloop()