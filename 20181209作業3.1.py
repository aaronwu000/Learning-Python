# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 21:01:24 2018

@author: Aaron
"""
"""
for i in range(3):
    print("*"*(i+1))
"""
#坐標系想法畫星號
s=""
N=15
for i in range(1,N+1):
    for j in range(1,N+1):
        if i+j>=N+1:
            s+="*"
        else:
            s+=" "
    s+="\n"
print(s)

