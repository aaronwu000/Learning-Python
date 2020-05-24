# -*- coding: utf-8 -*-
"""
Created on Sun May 19 20:36:19 2019

@author: Aaron
"""

import tkinter as tk

window=tk.Tk()
window.title("Menu")
window.geometry("500x500")

menubar=tk.Menu(window)


fileMenu=tk.Menu(menubar,tearoff=False)
fileMenu.add_command(label="開新遊戲")
fileMenu.add_command(label="作弊指令")
fileMenu.add_separator()
fileMenu.add_command(label="Exit",command=window.quit)#離開
menubar.add_cascade(label="檔案  ",menu=fileMenu)

fileMenu2=tk.Menu(menubar,tearoff=False)
fileMenu2.add_command(label="遊戲設定")
fileMenu2.add_command(label="畫面設定")
menubar.add_cascade(label="選項  ",menu=fileMenu2)


settings=tk.Menu(menubar,tearoff=False)
settings.add_command(label="遊戲優化Max")
settings.add_command(label="攻擊所有敵人")
fileMenu2.add_cascade(label="進階設定  ",menu=settings)

window.config(menu=menubar)


window.mainloop()