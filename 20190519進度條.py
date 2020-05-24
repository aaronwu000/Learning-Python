# -*- coding: utf-8 -*-
"""
Created on Sun May 19 19:49:35 2019

@author: Aaron
"""

import tkinter as tk

window=tk.Tk()
window.title("進度條")
window.geometry("600x300")

tk.Scale(window,label="進度條",
               orient=tk.HORIZONTAL,
               length=200).pack()

window.mainloop()