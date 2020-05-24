# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 20:51:06 2018

@author: Aaron
"""
row=int(input("輸入列數:"))
s=""
for i in range(1,row+1):
    for j in range(1,i+1):
        s+=str(j)
    s+="\n"
print(s,end="")
row-=1
s=""
for i in range(row,0,-1):
    for j in range(1,i+1):
        s+=str(j)
    s+="\n"
print(s)