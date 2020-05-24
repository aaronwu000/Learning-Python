# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 09:37:18 2019

@author: Aaron
"""

year=int(input("年:"))
month=int(input("月:"))
day=int(input("日:"))
print("year: " + str(year))
print("month: " + str(month))
print("day: " + str(day))

if month==1:
    plus_day=0
if month==2:
    plus_day=31
if month==3:
    plus_day=59
if month==4:
    plus_day=90
if month==5:
    plus_day=120
if month==6:
    plus_day=151
if month==7:
    plus_day=182
if month==8:
    plus_day=212
if month==9:
    plus_day=243
if month==10:
    plus_day=273
if month==11:
    plus_day=304
if month==12:
    plus_day=334

total=day+plus_day
if (year%4==0 and year%100!=0 or year%400==0) and total>60:
    total+=1
    print(print("It is the "+str(total)+"th day."))
else:
    print("It is the "+str(total)+"th day.")

