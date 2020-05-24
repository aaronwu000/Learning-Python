# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 19:08:48 2019

@author: Aaron
"""

#屬性 --> 名詞
#方法 --> 動詞

import turtle
def square():
    tur.fillcolor(1,0,1)
    tur.begin_fill()
    for _ in range(4):
        tur.forward(240)
        tur.right(90)
    tur.end_fill()

tur=turtle.Turtle()
turtle.setup(300,300)

tur.penup()
tur.goto(-120,120)
tur.pendown()
square()
turtle.done()
turtle.exitonclick()