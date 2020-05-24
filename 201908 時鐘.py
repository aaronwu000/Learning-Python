# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 20:24:44 2019

@author: Aaron
"""

from time import sleep
import datetime,turtle

def writenum(n):
    t.penup()
    t.forward(200)
    t.write(n)
    t.backward(200)
    t.pendown()

t=turtle.Turtle()
t.speed(0)
t.seth(90)
for i in range(12):
    t.right(30)
    writenum(i+1)

update = True
updateSecond = True
while True:
    now = datetime.datetime.now()
    h = now.hour%12
    m = now.minute
    s = now.second
    if update:
        hour=turtle.Turtle()
        hour.color(1, 0, 0)
        hour.seth(90)
        hour.right(h*30+m*0.5)
        hour.forward(100)
        min=turtle.Turtle()
        min.color(0, 0, 1)
        min.seth(90)
        min.right(m*6)
        min.forward(150)
        update=False
    if updateSecond:
        sec=turtle.Turtle()
        sec.seth(90)
        sec.right(s*6)
        sec.forward(200)
        updateSecond=False

    sleep(1)

    now = datetime.datetime.now()
    mNew = now.minute
    sNew = now.second
    if mNew != m:
        update=True
        hour.clear()
        hour.reset()
        min.clear()
        min.reset()
    if sNew != s:
        updateSecond=True
        sec.clear()
        sec.reset()

turtle.done()
turtle.exitonclick()