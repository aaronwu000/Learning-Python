# -*- coding: utf-8 -*-
"""
Created on Tue May 21 20:34:42 2019

@author: Aaron
"""


import tkinter as tk

window=tk.Tk()
window.title("Menu")
window.geometry("700x500")

menubar=tk.Menu(window)


fileMenu=tk.Menu(menubar,tearoff=False)
fileMenu.add_command(label="New file")
fileMenu.add_separator()
fileMenu.add_command(label="Open")
fileMenu.add_command(label="Open last closed")
fileMenu.add_command(label="Open recent")
menubar.add_cascade(label="File  ",menu=fileMenu)


fileMenu2=tk.Menu(menubar,tearoff=False)
fileMenu2.add_command(label="Undo")
fileMenu2.add_command(label="Redo")
menubar.add_cascade(label="Edit  ",menu=fileMenu2)
window.config(menu=menubar) 

fileMenu3=tk.Menu(menubar,tearoff=False)
fileMenu3.add_command(label="Find text")
fileMenu3.add_command(label="Find next")
fileMenu3.add_command(label="Find previous")
menubar.add_cascade(label="Search  ",menu=fileMenu3)
window.config(menu=menubar) 

fileMenu4=tk.Menu(menubar,tearoff=False)

settings=tk.Menu(menubar,tearoff=False)
settings.add_command(label="Carriage return and lind feed (Windows)")
settings.add_command(label="Line feed (UNIX)")
settings.add_command(label="Carriage return (Mac)")
fileMenu4.add_cascade(label="Convert end-of-line characters",menu=settings)
window.config(menu=menubar)

fileMenu4.add_command(label="Show blank spaces")
fileMenu4.add_command(label="Remove trailing spaces")
menubar.add_cascade(label="Source  ",menu=fileMenu4)
window.config(menu=menubar) 

fileMenu5=tk.Menu(menubar,tearoff=False)
fileMenu5.add_command(label="Run")
fileMenu5.add_command(label="Run cell")
fileMenu5.add_command(label="Run cell and advance")
menubar.add_cascade(label="Run  ",menu=fileMenu5)
window.config(menu=menubar)

fileMenu6=tk.Menu(menubar,tearoff=False)
fileMenu6.add_command(label="Debug")
fileMenu6.add_command(label="Step")
fileMenu6.add_command(label="Step into")
menubar.add_cascade(label="Debug  ",menu=fileMenu6)
window.config(menu=menubar)

fileMenu7=tk.Menu(menubar,tearoff=False)
fileMenu7.add_command(label="Open an Ippython console")
fileMenu.add_separator()
fileMenu7.add_command(label="Restart kernel")
fileMenu7.add_command(label="Connect to an existing kernel")
menubar.add_cascade(label="Consoles  ",menu=fileMenu7)
window.config(menu=menubar)

fileMenu8=tk.Menu(menubar,tearoff=False)
fileMenu8.add_command(label="New project")
fileMenu.add_separator()
fileMenu8.add_command(label="Open project")
fileMenu8.add_command(label="Close project")
menubar.add_cascade(label="Projects  ",menu=fileMenu8)
window.config(menu=menubar)

fileMenu9=tk.Menu(menubar,tearoff=False)
fileMenu9.add_command(label="Preferences")
fileMenu9.add_command(label="PYTHONPATH manager")
fileMenu9.add_command(label="Current user enviroment variables")
menubar.add_cascade(label="Tools  ",menu=fileMenu9)
window.config(menu=menubar)

fileMenu10=tk.Menu(menubar,tearoff=False)
fileMenu10.add_command(label="Panes")
fileMenu10.add_command(label="Lock panes")
fileMenu10.add_command(label="Close current pane")
menubar.add_cascade(label="View  ",menu=fileMenu6)
window.config(menu=menubar)

fileMenu11=tk.Menu(menubar,tearoff=False)
fileMenu11.add_command(label="Spyder documentation")
fileMenu11.add_command(label="Spyder tutorial")
fileMenu11.add_command(label="Shortcuts Summary")
menubar.add_cascade(label="Help  ",menu=fileMenu11)
window.config(menu=menubar)


window.mainloop()