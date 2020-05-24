# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 20:45:57 2019

@author: Aaron
"""
import tkinter as tk
import tkinter.font as tkf
import tkinter.messagebox





window=tk.Tk()
window.title("使用者登入")
window.geometry("500x300")

canvas=tkinter.Canvas(window,width=500,height=300)
image_file=tkinter.PhotoImage(file="mario.png")
print(image_file)
image=canvas.create_image(0,0,anchor="nw",image=image_file)

canvas.pack(side="top")



window.mainloop()