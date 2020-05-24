# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 19:36:02 2019

@author: Aaron
"""

for i in range(2,1001):

    allFactor=[]
    s=i
    for j in range(1,i):
        if i%j == 0:
            allFactor.append(j)
            s-=j
    if s==0:
        print("完全數: "+str(i))
        for k in allFactor:
            print(str(k),end=" ")
        print()
    
            