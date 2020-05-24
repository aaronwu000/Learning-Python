# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 20:11:15 2019

@author: Aaron
"""

def fun_age(n):
    s=0
    if n==1:
        s=10
    else:
        s=fun_age(n-1)+2
    return s

print(fun_age(5))
