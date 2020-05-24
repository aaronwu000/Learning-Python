# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 10:00:26 2019

@author: Aaron
"""
m=int(input("腳的數量:"))
n=int(input("動物個數:"))
chicken=round(n*2-m/2)
rabbit=round(n-chicken)
print("雞:"+str(chicken)+"   兔子:"+str(rabbit))