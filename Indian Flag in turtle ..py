# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 21:59:41 2023

@author: kotil
"""

from turtle import *
speed(1)
setup(800,500)
penup()
goto(-400,250)
pendown()
#orange rectangle
color("orange")
begin_fill()
forward(800)
right(90)
forward(167)
right(90)
forward(800)
end_fill()
#spacing
penup()
left(90)
forward(167)
left(90)
pendown()
#green rectangle
begin_fill()
color("green")
forward(800)
right(90)
forward(167)
right(90)
forward(800)
end_fill()
#big blue circle
penup()
goto(0,70)
pendown()
color("blue")
begin_fill()
circle(70)
end_fill()
#big white circle
penup()
goto(0,60)
pendown()
color("white")
begin_fill()
circle(60)
end_fill()
#miniblue circles
penup()
goto(7,-53)
pendown()
color("navy")
for i in range(24):
    begin_fill()
    circle(3)
    end_fill()
    penup()
    forward(14)
    right(15)
    
pendown()
#small blue circles
penup()
goto(0,20)
pendown()
begin_fill()
circle(20)
end_fill()
#spokes
penup()
goto(0,0)
pendown()
pensize(3)
for i in range(24):
    forward(60)
    backward(60)
    left(15)
    
