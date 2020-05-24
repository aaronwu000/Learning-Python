# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 07:53:54 2018

@author: Aaron
"""

running=True
while running:
    F=input("請輸入華氏溫度:")
    C=(int(F)-32)*5/9
    print("攝氏溫度為"+str(C)+"度")
    userIn=input("請問是否繼續(Y/N):")
    if userIn=="Y" or userIn=="y":
        running=True
    else:
        running=False
