# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 19:53:23 2018

@author: Aaron
"""

"""
for i in range(1,20):
    print("我是"+str(i)+"號")

threeTotal=0
for i in range(1,101):
    if i%3==0:
        threeTotal+=i
twoTotal=0
for i in range(1,101):
    if i%2==0:
        twoTotal+=i
sixTotal=0
for i in range(1,101):
    if i%6==0:
        sixTotal+=i
print(threeTotal+twoTotal-sixTotal)


for i in range(1,31):
    if i==5 or i==8:
        continue
    if i%19:
        break
    print(i)
    

count=0
while True:
    count+=1
    if count >20:
        break
    print(count)
 
    
a="10"
print(int(a)+10)


    
list1=[1,2,3,4,5,6,2,"b",2,"a",2,4,5,7,9,"a"]
if 4 in list1:
    print("有在裡面")
print(list1.count("a"))


a=1
b=1

a=b=1

a,b=1,2

allFactor=[]
count=0
for j in range(1,50):
    if 50%j == 0:
        count+=1
        allFactor.append(j)
"""

import tkinter as tk

window=tk.Tk()
window.title("登入")
window.geometry("600x300")

colours=["red","orange","yellow","green","blue","cyan","purple"]

r=0
for c in colours:
    tk.Label(window,text=c,width=15).grid(row=r,column=0)
    tk.Entry(window,width=15,bg=c).grid(row=r,column=1)
    r+=1
window.mainloop()
        

        
        
        
        