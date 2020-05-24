# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 19:27:29 2018

@author: Aaron
"""

total=0
for i in range(1,101):
    if i%2==0:
        total+=i
    elif i%3==0:
        total+=i
print(total)

