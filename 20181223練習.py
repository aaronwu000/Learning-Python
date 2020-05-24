# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 20:06:34 2018

@author: Aaron
"""
while True:
    n=int(input("1. 家庭好康餐\n2. 家庭超值餐\n3. 家庭豪華餐\n4. 離開\n請輸入: "))
    if n==4:
        break
    if n>=1:
        print("您可以觀賞的頻道是:\n台視\n中視\n華視")
    if n>=2:
        print("ELTA 影劇台\nELTA 戲劇台\nELTA 綜合台")
    if n>=3:
        print("Stars Movies HD\n福斯家庭電影台\nBBC Channel")
    print("--------------------------------------")
