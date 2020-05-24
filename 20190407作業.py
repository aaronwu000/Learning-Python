# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 20:56:07 2019

@author: Aaron
"""
"""
while 1: #1就是True
    try:
        a=input()
        print("hello, "+a) 
    except:
        break
"""


"""
#作業一 a003
while 1: 
    try:
        m,d = map(int,input().split())
        s =(m*2+d)%3
        if s==0:
            print("普通")
        elif s==1:
            print("吉")
        elif s==2:
            print("大吉")
    except:
        break
"""


"""
#作業二 a004
#西元年被4整除且不被100整除，或被400整除者即為閏年

while 1: 
    try:
        a=int(input())
        if a%4==0 and a%100!=0 or a%400==0:
            print("閏年")
        else:
            print("平年")
    except:
        break
"""


"""
#作業三 a005
lines=int(input())
for i in range(lines):
    a,b,c,d = map(int,input().split()) #map映射
    if a+c==b*2:
        e=d*2-c
    else:
        e=d*(d//c)
    print(a,b,c,d,e)
"""    
#2**3 二的三次方
"""
a022
#s[::-1] 把s字串倒過來
#作法一
while 1: 
    try:
        s=input()
        if s==s[::-1]:
            print("yes")
        else:
            print("no")
    except:
        break
        
#作法二
while 1: 
    try:
        s=input()
        print("yes" if s==s[::-1] else "no")
    except:
        break
"""

"""
import math
while 1: 
    try:
        a,b = map(int,input().split())
        print(math.gcd(a,b))
    except:
        break
"""


