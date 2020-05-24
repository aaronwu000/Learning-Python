# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 19:29:10 2019

@author: Aaron
"""

result=0
temp=1
for i in range(1,21):
    temp*=i
    result+=temp
print("1!+2!+3!+...+20! = "+str(result))