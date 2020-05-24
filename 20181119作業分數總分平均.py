# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 20:54:52 2018

@author: Aaron
"""
subject=["國文","英文","數學"]
userIn="Y"
while userIn=="Y" or userIn=="y":
    total=0
    for i in subject:
        wrong=True
        while wrong:
            try:
                score=int(input("請輸入"+i+"分數:"))
                if (score)>=0 and (score)<=100:
                    wrong=False
                    total+=score
                else:
                    print("範圍錯誤!請輸入正確分數範圍")
                    wrong=True
            except ValueError:
                print("請輸入阿拉伯數字")
    average=round(total/3,2)
    print("總分:"+str(total))
    print("平均:"+str(average))
    userIn=input("請問是否繼續(Y/N):")