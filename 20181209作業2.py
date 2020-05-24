# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 21:19:43 2018

@author: Aaron
"""
"""
n=int(input("請輸入數字:"))
a=1
b=0
while a<n:
    b+=a*(a+1)
    a+=1
print(b)
"""

n=int(input("請輸入數字:"))
s=0
for i in range(n+1):
    s+=i*(i-1)
print(s)