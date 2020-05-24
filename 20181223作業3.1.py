# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 20:47:08 2018

@author: Aaron
"""

s=""
for i in range(1,6):
    for j in range(1,i+1):
        s+="*"
    s+="\n"
print(s)