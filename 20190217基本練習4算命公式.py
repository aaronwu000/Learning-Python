# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 19:32:16 2019

@author: Aaron
"""

m=int(input("月:"))
d=int(input("日:"))
s=(m*2+d)%3
if s==0:
    print("普通")
if s==1:
    print("吉")
if s==2:
    print("凶")