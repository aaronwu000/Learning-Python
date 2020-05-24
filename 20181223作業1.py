# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 10:16:32 2019

@author: Aaron
"""
"""
s=""
a=0
b=0
for i in range(1,10):
    a+=1
    b=0
    for j in range(1,10):
        b+=1
        s+=str(a)+"*"+str(b)+"="+str(a*b)+"\t"
    s+="\n"
print(s)
"""
s=""
for i in range(1,10):
    for j in range(1,10):
        #s+=str(j)+"*"+str(i)+"="+str(i*j)+"\t"
        s=i*j
        print ("%d*%d=%d" %(i, j , s),end="\t")
    print()
#print(s)