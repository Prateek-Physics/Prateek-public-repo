# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 14:31:52 2023

@author: prateek

"""
from sympy import *
init_printing()
def sin(x):
 import numpy as np
 y=(np.pi/180)*x
 return np.sin(y)
def cos(x):
    import numpy as np
    y=(np.pi/180)*x
    return np.cos(y)
def tan(x):
    import numpy as np
    y=(np.pi/180)*x
    return np.tan(y)
def cosec(x):
    import numpy as np
    y=(np.pi/180*x)
    return 1/np.sin(y)
def sec(x):
    import numpy as np
    y=(np.pi/180)*x
    return 1/np.cos(y)
def cot(x):
    import numpy as np
    y=(np.pi/180)*x
    return 1/np.tan(y)
def ln(x):
    import numpy as sp
    y=sp.log(x)
    return y
def log(x):
    import math
    y=math.log10(x)
    return y
def fact(x):
    f=1
    while x>0:
        f=f*x
        x=x-1
    return f
def pi():
    return 3.14159265358979323846
def derivate():
    print("YOU WANT SOLUTION AS A FUNCTION OR VALUE OF THAT FUNCTION ON A POINT ??")
    print('')
    print("")
    print("PRESS 1 FOR FUNCTION AND PRESS 2 FOR VALUE OF FUNCTION AT A POINT")
    
    for i in range(100):
     d=eval(input("ENTER 1 OR 2 : "))
     print("")
     print("")
     if d==1:
         derivate_analytically()
         break
     if d==2:
         derivate_numerically()
         break
     else:
         print("WRONG NUMBER PRESSED , PRESS EITHER 1 OR 2 ")
         continue
         
        

def random(x,y):
 import random as rd
 return (rd.randint(x,y))
#######################################################################################
#BASIC CODE TO DELETE PREVIOUS INPUT ENTRY AND INSERT A NEW ONE
def plotgraph():
 import matplotlib.pyplot as pl
 
 x1=[]
 y1=[]
 o=1
 n=int(input("HOW MANY POINT SETS YOU NEED TO PLOT ?? :"))
 k=n
 print("IF YOU ENTER A WRONG ENTRY JUST PRESS D/d ON NEXT ENTRY ")
 
 while n>0:
    
    
    print("FOR X ENTER VALUE ",end=" ")
    print(o,end=":")
    i=input("----------------> ")
    
    
    if i=="d" or i=="D": # if d is pressed last value added to list will be deleted and curser will again shifted at that value so that you can add new value there
        x1.pop()
        n=n+1
        o=o-1   
        continue
    else:
        x=float(i)
        x1.append(x)
        n=n-1
        o=o+1
 print(x1)

 q=1   
 while k>0:

    print("FOR Y ENTER VALUE",end=" ")
    print(q,end=" ")
    j=input(":")
    
    
    if j=="d" or j=="D": 
        y1.pop()
        k=k+1
        q=q-1   
        continue
    else:
        y=float(j)
        y1.append(y)
        k=k-1
        q=q+1
 print(y1)
 
 a=input("ENTER TITLE OF THE GRAPH YOU WANT TO PUT ?? :")
 b=input("ENTER THE TITLE OF X AXIS :")
 c=input("ENTER THE TITLE OF Y AXIS:")
 g=input("YOU WANT TO DISPLAY GRID ?? (YES/NOT) :")
 
 if g=="yes" or g=="YES":
     print("visible")
     pl.grid(3)
 else:
     print("not visible")
     
 
     
 pl.plot(x1,y1)
 pl.xlabel(b)
 pl.ylabel(c)
 pl.title(a)
 pl.show()
 #####################################################################################
def solve_equation():
    import numpy as np
    import scipy as sp
    import sympy as smp
    from scipy.integrate import quad
    x=smp.symbols('x',real=True)
    z1=eval(input("ENTER EQUATION YOU WANT TO SOLVE NUMERICALLY LIKE(x**2-1) : "))
    bisection(z1)
    newtonraphson(z1)
    sympymethod(z1)
    bruteforce(z1)
 #############################################################################
#This code uses bisection method 
def bisection(z1):
  try:
   import matplotlib.pyplot as pl   
   import numpy as np
   import scipy as sp
   import sympy as smp
   from scipy.integrate import quad
   %matplotlib
   x=smp.symbols('x',real=True)
   r=z1
   f=smp.lambdify(x,r)
   a=-101#initial range
   b=100#final range 
   c=(a+b)/2
   
   for i in range(100):
       
       
       if f(c)>0:
        a=a
        b=(a+b)/2
         
       elif(f(c)<0):
        a=(a+b)/2
        b=b
        
       c=(a+b)/2
       
   if  f(c)>0.000001:
       print("WRONG BOUNDS ENTERED . TRY INCREASING INITIAL AND FINAL RANGE")
   elif(f(c)==0):
       print('1) USING BISECTION METHOD SOLUTION  IS =',c)
   else:
       print("")
       print("")
       print("USING BISECTION METHOD SOLUTION  CALCULATED IS :",c)
   t=np.linspace(-50,50,10000)  
   y=f(t)
   pl.plot(t,y)
   pl.axvline(x=c, color='red', label='x =')
   pl.axhline(y=0,color='blue',label='y=0')
   
   pl.ylabel("y axis")
   pl.xlabel("x axis")
   pl.ylim(-50,50)
   pl.xlim(-50,50)
   pl.show()
   return c
  except:
      print("BISECTION METHOD FAILED")
################################################################################
def newtonraphson(z1):
 import sympy as smp
 import scipy as sp
 x=smp.symbols('x',real=True)
 y=z1
 f=smp.lambdify(x,y)
 ydx=smp.diff(y,x)
 fdx=smp.lambdify(x,ydx)
 x0=eval(input("Enter guess value for N-R METHOD :"))
 #xn=x0-f(x0)/f(x0)
 try:
   for n in range(1000):
    xn=x0-f(x0)/fdx(x0)
    x0=xn
   print("2) USING NEWTON RAPHSON METHOD ANSWER IS :",xn) 
   print("")
 except:
     raise NameError("Newton-Raphson method failed")
######################################################################################
def sympymethod(z1):
 import sympy as smp
 import scipy as sp
 import numpy as np
 try:
  x = smp.Symbol('x')
  equation=z1
  roots = smp.roots(equation)
  print("USING SYMPY")
  print("SOLUTIONS ARE :")
  print("")
  for root in roots:
    print("x=",root)
    print("")
 except:
    print("SYMPY METHOD FAILED")
    
 try:
   x = smp.Symbol('x')
   equation=z1
   roots = smp.roots(equation)
   print("USING SYMPY")
   print("EXACT SOLUTIONS ARE :")
   print("")
   for root in roots:
     print("x=",root.evalf())
     print("")
 except:
     print("SYMPY METHOD FAILED")
  
#################################################################################
def bruteforce(z1):
 import sympy as smp
 import time as t
 x=smp.symbols('x',real=True)
 f=z1
 y=smp.lambdify(x,f)  

 def is_close_to_zero(number, threshold=1e-4):
     return abs(number) < threshold
 print("")
 print("Wait i am calculatin using brute force method ........")
 n=-100
 ans=[]
 s=t.time()
 while n<=100:
     
     if y(n)==0 or (is_close_to_zero(y(n))):
         
         ans.append(n)
         n=n+0.00001
         
     else:
         pass
         n=n+0.00001
 print("")
 f=t.time()
 print("")
 lst=ans
 rounded=[round(num, 4) for num in lst]
 original_list = rounded

 unique_list = list(set(original_list))
 
 print('This Equation has',len(unique_list),"solutions using brute force method")

 for i in unique_list:
    print(" Using brute force method x  is :",i)
 print("Time Taken : ",f-s,"seconds")
####################################################################################

  
#####################################################################################

def derivate_analytically():
 import numpy as np
 import scipy as sp
 import sympy as smp
 from scipy.misc import derivative
 x=smp.symbols('x',real=True)
 f=eval(input("ENTER FUNCTION WHOSE DERIVATIVE IS NEEDED AS EXPRESSION : "))
 print("")
 print("")
 f_1=smp.diff(f,x).simplify()
 print("The derivative of",f,"is = ",f_1)
 return f_1




def derivate_numerically():
    import time
    import numpy as np
    import scipy as sp
    import sympy as smp
    from scipy.misc import derivative
    x=smp.symbols('x',real=True)
    f=eval(input("ENTER FUNCTION f(x) WHOSE DERIVATIVE IS NEEDED AS NUMERIC VALUE : "))
    print("")
    print("")
    print("")
    print("IF VALUE OF DERIVATIVE NEEDED AT A SINGLE POINT , PRESS - 1 ")
    print("")
    print("")
    print("")
    print("IF VALUE OF DERIVATIVE BETWEEN TWO POINTS IS NEEDED , PRESS - 2 ")
    print("")
    print("")
    print("")
    
    print("")
    print("")
    print("")
    for i in range(100):
     p=eval(input("PRESS 1 OR 2 : "))
     if p==1:
      point1=eval(input("ENTER POINT AT WHICH VALUE OF DERIVATIVE IS NEEDED : "))
      print("")
      print("")
      s1=time.time()
      f_1=smp.diff(f,x).simplify()
      f_1_at_a_point=smp.lambdify(x,f_1)
      e1=time.time()
     
   
      print("THE VALUE OF f'(x) AT",point1,"is =",f_1_at_a_point(point1))
      print("")
      print("THE VALUE OF ",f_1," AT",point1,"is =",f_1_at_a_point(point1))#f_1_at_a_point=f'(x)
      print("")
      print("")
      print("THE TIME TAKEN IN CALCULATION IS = ",e1-s1)
      return f_1_at_a_point(point1)
      break
     if p==2:
      a=eval(input("ENTER LOWER LIMIT : "))
      print("")
      print("")
      b=eval(input("ENTER UPPER LIMIT : "))
      print("")
      print("")
      s1=time.time()
      f_1=smp.diff(f,x).simplify()
      f_1_at_a_point=smp.lambdify(x,f_1)
      d=f_1_at_a_point(b)-f_1_at_a_point(a)
      e1=time.time()
      print("THE VALUE OF",f_1,"BETWEEN",a,"AND",b,"IS =",d)
      print("THE TIME TAKEN IN CALCULATION IS = ",e1-s1)
      return d
      break
     else:
         print("WRONG NUMBERS ENTERED , ENTER EITHER 1 OR 2 ONLY ")
         continue
        
        
 ######################################################################################
 
def integrate():
 import numpy as np
 import scipy as sp
 import sympy as smp
 from scipy.integrate import quad
 x,a,b=smp.symbols('x,a,b',real=True)
 
 f=eval(input("ENTER FUNCTION WHOSE INTEGRAL IS NEEDED : "))
 print("")
 print("")
 print(" IF YOU NEED INTEGRAL AS EXPRESSION PRESS - 1 ")
 print("")
 print("")
 print(" IF YOU NEED ANSWER AS AREA UNDER THE CURVE PRESS - 2 ")
 print("")
 print("")
 for i in range(100):
  q1=eval(input(" ENTER 1 OR 2 :"))
 
  if q1==1:
     
   print("")
   print("")
   fdx=smp.integrate(f,x).simplify()
   print("THE INTEGRAL OF f(x) is = ",fdx)
   print("")
   print("")
   print("THE INTEGRAL OF ",f," is = ",fdx)
   return fdx
   break
  if q1==2:
   r=eval(input("ENTER LOWER LIMIT :"))
   s=eval(input("ENTER UPPER LIMIT :"))
   print("")
   print("")
   fdx=smp.integrate(f,(x,r,s)).evalf()
   print("The Area under curve (",f,") between",r,"and",s,"is = ",fdx)
   print("")
   return fdx
   break
  else:
      print("WRONG NUMBER ENTERED.ENTER EITHER 1 OR 2 ONLY !!")
      continue

 #######################################################################################
print("WELCOME ")
print("")
print("")
print("")




def helpme():
    print("integrate() ---> TO INTEGRATE ANY FUNCTION USE THIS FUNCTION")
    print("derivate_numerically()-------> TO SOLVE A DEFINITE INTEGRAL USE THIS FUNNCTION")
    print("derivate_analytically()------> TO SOLVE INDEFINITE INTEGRAAL USE THIS FUNCTION")
    print("solve_equation_numerically()--------> TO GET ATLEAST ONE SOLUTION OF AN EQUATION IN ONE VARIABLE USING BISECTION METHOD USE THIS FUNCTION")
    print("plotgraph()------------> TO INPUT POINTS FOR X AXIS AND Y AXIS AND PLOT A GRAPH BETWEEN THEM USE THIS FUNCTION")
    print("log(x)-----> TO CALCULATE LOG TO THE BASE 10 USE THIS FUNCTION")
    print("ln(x)------> TO CALCULATE LOG TO THE BASE e USE THIS FUNCTION ")
    print("fact(x)----> TO CALCULATE  FACTORIAL OF A NUMBER USE THIS FUNCTION")
    print("pi()-------> TO GET THE EXACT VALUE OF PI UPTO 15 DECIMAL POINTS  USE THIS FUNCTION")
    print("sin(x)")
    print("cos(x)")
    print("tan(x)")
    print("cosec(x)")
    print("sec(x)")
    print("cot(x)")



###########       working area begins *******************
solve_equation()


    