# -*- coding: utf-8 -*-
"""
Created on Sun May 19 14:18:29 2019

@author: Aaron
"""
import math
while 1: 
    try:
        a,b = map(int,input().split())
        print(math.gcd(a,b))
    except:
        break

