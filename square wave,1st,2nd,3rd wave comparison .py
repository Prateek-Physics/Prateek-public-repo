
"""
code-3 

Square wave analysis in Python , This code generates first ,second and third wave of fourier series for square wave and compares thier amplitude and frequency.

"""
import matplotlib.pyplot as plt
import numpy as np
from sympy import *
%matplotlib
A=1
T=1
def f1(x):
    return (4*A/np.pi)*np.sin(np.pi*x/T)
def f2(x):
    return (4*A/(3*np.pi))*np.sin(3*np.pi*x/T)
def f3(x):
    return (4*A/(5*np.pi))*np.sin(5*np.pi*x/T)
x=np.linspace(0,5,1000)
a=f1(x)
b=f2(x)
c=f3(x)
plt.plot(x,a,'b')
plt.plot(x,b,'r')
plt.plot(x,c,'cyan')
plt.grid(True)
plt.legend(['First wave',"Second wave","Third wave"],loc="upper right")
