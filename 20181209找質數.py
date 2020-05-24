# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 19:52:21 2018

@author: Aaron
"""
import math
i=2
while i<100:
    a=2
    flag=True
    while a<=math.sqrt(i): #找出最漂亮方式 #1,一半以下 2,開根號
        if i%a==0:
            #合數
            flag=False
            break
        a+=1
    if flag:     
        print(str(i)+"為質數")        
    i+=1