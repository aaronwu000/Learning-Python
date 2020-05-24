# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 20:20:34 2018

@author: Aaron
"""

x=int(input("X:"))
y=int(input("Y:"))


s=""
for i in range(1,6):
    for j in range(1,11):
        if i==x and j==y:
            s+="x "
        else:
            s+="o "
    s+="\n"
print(s)