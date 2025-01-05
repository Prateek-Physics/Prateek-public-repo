# sawtooth wave  fourier series f(x)=x,0<x<2*pi
import matplotlib.pyplot as plt
import numpy as np
import sympy as smp
pi=np.pi
x,n=smp.symbols('x n',real=True)
p=x
n=5
t=np.linspace(-12,12,100)
l1=-pi
sum1=0
l2=pi
a0=smp.integrate((x/pi),(x,l1,l2)).evalf()
print("a0 is :",a0)
for i in range(1,n+1):
 an=smp.integrate((p*smp.cos(n*p))/pi,(x,l1,l2)).simplify()
 A=an*smp.cos(n*x)
 bn=smp.integrate((p*smp.sin(i*p))/pi,(x,l1,l2)).simplify()
 B=bn*smp.sin(i*x)
 sum1=sum1+B+A
 sum=sum1+a0/2
 f=smp.lambdify(x,sum)
 plt.plot(t,f(t))
plt.xlabel("$x$")
plt.ylabel("$f(x)$")
plt.title("SAWTOOTH WAVE")

