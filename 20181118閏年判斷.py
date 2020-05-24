# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 21:04:02 2018

@author: Aaron
"""
"""
#方法一
year = int(input("請輸入年份："))
if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            print ("潤年")
        else:
            print ("平年")
    else:
        print ("潤年")
else: 
    print ("平年”)
"""
"""
#方法二
year=int(input("請輸入年分:"))
if year%400 ==0 or year%4 ==0 and year%100!=0:
    print("閏年")
else:
    print("平年")

import calender
year=int(input("請輸入年分:"))
check_year=calender.isleap(year)
if check_year:
    print("閏年")
else:
    print("平年")
    
"""

while True:
    print("hi")