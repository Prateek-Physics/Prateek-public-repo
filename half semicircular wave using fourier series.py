# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 14:26:21 2023

@author:PRATEEK
"""

import matplotlib.pyplot as plt
import numpy as np
import sys as s
%matplotlib

pi=np.pi
T=eval(input("Enter time period:"))/2 #2T is the period of wave , so we need to give half value in T
r=eval(input("Enter Amplitude:"))
N=eval(input("Enter Number of terms:"))
if T>r:
    print('Amplitude must be greater than time period') 
    s.exit()
    
x=np.linspace(0, 2*T, 1000)
def a0_():
 y=(1/T)*((np.sqrt(r**2-x**2)))
 a0 = np.trapz(y, x)
 return a0

def an_(n):
 y=(1/T)*(np.sqrt(r**2-x**2)*np.cos(n*pi*x/T))
 an = np.trapz(y, x)
 return an

def bn_(n):
 y=(1/T)*(np.sqrt(r**2-x**2)*np.sin(n*pi*x/T))
 bn = np.trapz(y, x)
 return bn
a0_value=a0_()
an_values=[an_(i) for i in range(1,N+1) ] 
bn_values=[bn_(i) for i in range(1,N+1) ]
print(a0_value,an_values,bn_values)


def f(x):
    sum=0
    for n in range(1,N+1):
        sum += an_values[n-1]*np.cos(n*pi*x/T) + bn_values[n-1]*np.sin(n*pi*x/T)
    return (sum+a0_value/2)

a=np.linspace(0,10,1000)
b=[f(i) for i in a]
plt.plot(a,b,'b')
plt.grid()
plt.title('Semicircular wave by fourier series')
plt.xlabel('$x$')
plt.ylabel('$f(x)$')

