# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 19:37:39 2019

@author: Aaron
"""

import turtle

def rec():
    t.begin_fill()
    for _ in range(2):
        t.forward(400)
        t.right(90)
        t.forward(100)
        t.right(90)
    t.end_fill()
def mygoto(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    

t=turtle.Turtle()
turtle.setup(430,430)

mygoto(-200,150)
t.fillcolor(0,0,0)
rec()

mygoto(-200,50)
t.fillcolor(1,0,0)
rec()
    
mygoto(-200,-50) 
t.fillcolor(1,1,0)
rec()


turtle.done()
turtle.exitonclick()