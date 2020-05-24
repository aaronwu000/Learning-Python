# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 19:34:40 2019

@author: Aaron
"""
"""
row=int(input("輸入列數:"))
for i in range(1,row+1):
    for j in range(1,row-i+1):
        print(" ",end="")
    print("*"*(i*2-1))
"""


#2n-1
    
"""
----*
---***
--*****
-*******
*********
----1
---232
--34543
-4567654
567898765
"""
k=count=count1=0
row=int(input("輸入列數:"))
for i in range(1,row+1):
    for j in range(1,row-i+1):
        print(" ",end="")
        count+=1
    while k != i*2-1:
        if count<=row-1:
            print(i+k,end="")
            count+=1
        else:
            count1+=1
            print(i+k-2*count1,end="")      
        k+=1    
    k=count=count1=0
    print()
    
    
        