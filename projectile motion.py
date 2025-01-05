# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 18:59:55 2023

@author:prateek baba
"""
import math
import matplotlib.pyplot as pl
def drawgraph(x,y):
    pl.xlabel("Horizontal Distance")
    pl.ylabel("Vertical Distance")
    pl.title("Projectile Motion of object thown with 30m/s")
    pl.plot(x,y,'--o')
def myrange(start,end,interval):
    num=[]
    while start<end:
        num.append(start)
        start+=interval
        
    return num

def drawprojectile(u,theta):
    theta=math.radians(theta)
    g=9.8
    #time
    t=2*u*math.sin(theta)/g
    print(t)
    #integral
    intervals=myrange(0,t,0.001)
    x=[]
    y=[]
    for t in intervals:
        x.append(u*math.cos(theta)*t)
        y.append(u*math.sin(theta)*t-0.5*g*t*t)
    drawgraph(x,y)
u=30
tlist=[0,20,30,40,45,50,60,70,90]
for t in tlist:
    drawprojectile(u,t)
    
pl.legend(['0','20','30','40','45','50','60','70','90'])
pl.show()
