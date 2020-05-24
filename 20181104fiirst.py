# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 20:51:07 2018

@author: Aaron
"""
"""
aScore=20
bScore=100
cScore=10

if(aScore >= 80):
    print("A等")
elif(aScore >= 60):
    print("B等")
elif(aScore >= 0):
    print("C等")
print("ASCII 48: "+chr(48))
print("ASCII a: " + str(ord("a")))

account=input("帳號:")
password=input("密碼:")
print(account+","+password)


chScore=input("請輸入國文分數:")
maScore=input("請輸入數學分數:")
print("總分:"+str(int(chScore)+int(maScore))+"分")

import math
print(math.pow(2,10))
print(math.sqrt(9))

c=input("請輸入攝氏:")
f=int(c)*9/5+32
print("華氏為:"+str(f))

a = input("請輸入a:")
b = input("請輸入b:")

c = a % b #求餘數

print("a = "+str(a))
print("b = "+str(b))
print("c = "+str(c))

result = c == 0 
print(str(a)+"是"+str(b)+"的倍數？"+str(result))


a=10
b=5
if a%b ==0:
    print(str(a)="是"+str(b)+"的倍數")
else:
    print(str(a)="不是"+str(b)+"的倍數")
    


month = int(input("請輸入月份："))

if month<1 or month>12 :
    print("請輸入正確月份！！！")

if month>0 and month<13 :
    print("輸入正確！！！")
else:
    print("請輸入正確月份！！！")
          

if not month>0 and month<13 :
    print("請輸入正確月份！！！")
else:
    print("輸入正確！！！")




year=int(input("請輸入年分:"))
if year%400 ==0 or year%4 ==0 and year%100!=0:
    print("閏年")
else:
    print("平年")
"""
    

print(round(2.33323456,2))