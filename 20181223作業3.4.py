# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 20:52:22 2018

@author: Aaron
"""

s=""
for i in range(1,5):
    for j in range(1,i+1):
        s+=str(j)
    s+="\n"
for i in range(1,6):
    for j in range(1,i+1):
        if i==1:
            break
        else:        
            s+=str(j)
    s+="\n"
for i in range(1,7):
    for j in range(1,i+1):
        s+=str(j)
    s+="\n"
print(s)