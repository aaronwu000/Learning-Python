# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 19:03:39 2019

@author: Aaron
"""

def fact(n):
    result=0
    if n==0:
        result=1
    else:
        result=n*fact(n-1)
    return result
for i in range(5):
    print(str(i)+"! = "+str(fact(i)))