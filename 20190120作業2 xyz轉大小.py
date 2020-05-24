# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 08:08:02 2019

@author: Aaron
"""
"""
#法一
x=int(input("x:"))
y=int(input("y:"))
z=int(input("z:"))
if x>y:
    x,y=y,x #swap
if x>z:
    x,z=z,x
if y>z:
    y,z=z,y
print(str(x)+","+str(y)+","+str(z))
"""
#法二:氣泡排序法(bubble sort)


def bubble_sort(l):
    for i in range(1,len(l)): #有n-1回合
        for j in range(len(l)-i): #每回合比較範圍
            print(len(l)-1-i)
            print("j:"+str(j))
            if l[j]>l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]
    print(l)
mylist=[4,87,97,56,43,32]
bubble_sort(mylist)



