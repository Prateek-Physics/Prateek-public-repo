# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 13:12:11 2024

@author: Prateek
"""

%matplotlib
import numpy as np
import matplotlib.pyplot as plt 
x=np.linspace(0,13,1000)
y1=6*(1-np.exp(-x))
plt.plot(x,y1)
y2=6*(np.exp(-x))
y3=(12/np.sqrt(3))*np.sin(np.sqrt(3)/3 * x)*np.exp(-0.5*x)
plt.plot(x,y2)
plt.plot(x,y3)
plt.legend(['y1(RL circuit)','y2(RC circuit)',"y3 RLC"])
plt.xlabel("time",fontsize=16)
plt.ylabel("Current",fontsize=16)
plt.grid(True)
