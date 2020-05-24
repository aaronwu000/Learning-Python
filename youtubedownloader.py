# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 20:02:48 2019

@author: Aaron
"""

#串流stream
#圖片解析度 image resolution
#幀率 fps frame per second
from pytube import YouTube
import tkinter as tk
progress=0

def showProgress(stream,chunk,file_handle,bytes_remaining):
    size=stream.filesize
    global progress
    preProgress=progress
    progress=(size-bytes_remaining)*100//size
    
    if preProgress != progress:
        scale.set(progress)
        window.update()
        print("目前進度:"+ str(progress)+ "%") 
    if progress==100:
        print("下載完成")
        return #結束函式了

def onClick():
    global var
    var.set(en.get())
    try:
        yt=YouTube(var.get(),on_progress_callback=showProgress)
        stream=yt.streams.filter(res="720p").first()
        stream.download("youtube影片",yt.title)
    except:
        print("下載失敗")
        
window = tk.Tk()
window.title("YouTube下載器")
window.geometry("500x150")
window.resizable(False,False)

tk.Label(window,text="請輸入YouTube影片網址:").pack()
var=tk.StringVar()
en=tk.Entry(window,width=50)
en.pack()
tk.Button(window,text="下載",command=onClick).pack()
scale=tk.Scale(window,label="進度條",from_=0,to=100,orient=tk.HORIZONTAL,length=200,tickinterval=0)
scale.pack()




menubar=tk.Menu(window)

fileMenu=tk.Menu(menubar,tearoff=False)
fileMenu.add_command(label="開新遊戲")
fileMenu.add_command(label="作弊指令")
fileMenu.add_separator()
fileMenu.add_command(label="Exit")
menubar.add_cascade(label="檔案  ",menu=fileMenu)

fileMenu2=tk.Menu(menubar,tearoff=False)
fileMenu2.add_command(label="遊戲設定")
fileMenu2.add_command(label="畫面設定")
menubar.add_cascade(label="選項  ",menu=fileMenu2)
window.config(menu=menubar) #config 配置設定




window.mainloop()

