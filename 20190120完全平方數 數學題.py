  # -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 20:32:58 2019

@author: Aaron
"""
"""
一個整數，加上100後是一個完全平方數，再加上168又是一個完全平方數，該數為?
設該數為x
x+100=n平方，x+268=m平方
(m+n)(m-n)=168
m+n=i，m-n=j，i*j=168(i和j至少有一個偶數)
m=(i+j)/2，n=(i-j)/2(i和j皆為奇數或皆為偶數)
===>i和j 都是大於等於2的偶數
1<i<85
"""

for i in range(2,85):
    if 168%i==0:
        j=168/i
        if (i+j)%2==0 and (i-j)%2==0 and i>j:
            m=(i+j)/2
            n=(i-j)/2
            x=n*n-100
            print(x)
            
        
        
        
        
        
        