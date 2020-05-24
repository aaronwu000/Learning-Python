# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 09:09:48 2019

@author: Aaron
"""

import turtle

def rec():
    t.begin_fill()
    for _ in range(2):
        t.forward(120)
        t.right(90)
        t.forward(300)
        t.right(90)
    t.end_fill()


def mygoto(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown


t=turtle.Turtle()
turtle.setup(430,430)


mygoto(-200,150)
t.fillcolor(0,0,1)
rec()

mygoto(-80,150)
t.fillcolor(1,1,1)
rec()

mygoto(40,150)
t.fillcolor(1,0,0)
rec()




turtle.done()
turtle.exitonclick()