# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 20:28:27 2019

@author: Aaron
"""
s=0
for i in range(1,11):
    if i%2==1:
        s+=i
    if i%2==0:
        s-=i
print(s)