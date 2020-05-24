# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 20:53:18 2018

@author: Aaron
"""
#費氏數列(Fibonacci) #Recursive(遞迴)
number1=0
number2=1
myStr=""
while number1+number2<100:
    myStr=myStr+" "+str(number1)+" "+str(number2)
    nextNumber1=number1+number2
    nextNumber2=number2+nextNumber1
    number1=nextNumber1
    number2=nextNumber2
print(myStr)