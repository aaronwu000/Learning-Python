# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 20:38:28 2018

@author: Aaron
"""

# 1 剪刀
# 2 石頭
# 3 布
import random
while True:
    r=random.randrange(1,4)
    player=int(input("1.剪刀\n2.石頭\n3.布\n4.結束\n請輸入:"))
    print("Computer:"+str(r))
    print("Player:"+str(player))
    if player==4:
        break    
    elif r==player:
        print("平手!")
    elif r==1 and player==2 or r==2 and player==3 or r==3 and player==1:
        print("你贏了!")
    else:
        print("你輸了!")
    print("------------------------")