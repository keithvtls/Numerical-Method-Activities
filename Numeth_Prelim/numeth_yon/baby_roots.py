#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt


# In[ ]:


### brute force algorithm (f(x)=0)
def f_of_x(f,roots,tol,i, epochs=100):
  
    # f = eq # equation to be solved
    x_roots=[] # list of roots
    n_roots= roots # number of roots needed to find
    incre = i #increments

    # end_epochs= stop_epochs #ending point of the iteration
    # epochs= start_epochs #starting point of the iteration
    h = tol #tolerance is the starting guess

    for epoch in range(epochs): # the list of iteration that will be using
     if np.isclose(f(h),0): # applying current h or the tolerance in the equation and the approximation on f(x) = 0
        x_roots.insert(len(x_roots), h) 
        end_epochs = epoch
        if len(x_roots) == n_roots:
          break # once the root is found it will stop and print the root
     h+=incre # the change of value in h wherein if the roots did not find it will going to loop
   
    return x_roots, end_epochs # returning the value of the roots and the iteration or the epochs


# In[ ]:


### brute force algorithm (in terms of x)
def in_terms_of_x(eq,tol,epochs=100):

    funcs = eq # equation to be solved
    x_roots=[] # list of roots
    n_roots = len(funcs) # How many roots needed to find according to the length of the equation
    # epochs= begin_epochs # number of iteration
    h = tol # tolerance or the guess to adjust

    for func in funcs:
      x = 0 # initial value or initial guess
      for epoch in range(epochs): # the list of iteration that will be using
        x_prime = func(x)
        if np.allclose(x, x_prime,h): 
          x_roots.insert(len(x_roots),x_prime)
          break # once the root is found it will stop and print the root
        x = x_prime
    return x_roots, epochs # returning the value of the roots and the iteration or the epochs


# In[ ]:


### newton-raphson method
def newt_raphson(f,f_prime, x_inits, epochs=100):

  roots = [] # list of roots

  for x_init in x_inits:
    x = x_init
    for epoch in range(epochs):
      x_prime = x - (f(x)/f_prime(x))
      if np.allclose(x, x_prime):
        roots.append(x)
        break # once the root is found it will stop and print the root
      x = x_prime
  return roots, epochs # returning the value of the roots and the iteration or the epochs


# In[ ]:


### Bisection Method
def bisection(f, i1, i2, steps, h=1e-06, end_bisect = 0):
  y1, y2 = f(i1), f(i2) # Calculated values of y1 and y2 given i1 and i2                                  
  roots = [] # list of roots 
  if np.sign(y1) == np.sign(y2): # Check the signs of y are different                           
    print("Root cannot be found in the given interval") # If the signs of y1 and y2 are the same halt
  else:
    for i in steps: # steps for the interval of i1 and i2
      int1 = i1+i # interval 'i1' will become 'int1'
      int2 = i2+i # interval 'i2' will become 'int2'
      intval = int1, int2 # making it a tuple
      for bisect in range(0,100):                               
        midp = np.mean(intval) # If the signs of y1 and y2 are opposite, calculate the x in the half of the interval                                #5
        y_mid = f(midp) 
        y1 = f(int1)
        if np.allclose(0,y1, h): # If y1 and y2 approach 0, halt.
          roots.append(int1)
          end_bisect = bisect
          break
        if np.sign(y1) != np.sign(y_mid): #root is in first-half interval
          i2 = midp
        else: #root is in second-half interval
          i1 = midp 
  if roots is not None:
    return roots, end_bisect


# In[ ]:


### Regula Falsi Method
def falsi(f, a, b, steps, h=1e-06, pos=0):
  y1, y2 = f(a), f(b) # Calculate values of y1 and y2 given a and b.
  roots = [] # list of roots 
  if np.allclose(0,y1): root = a
  elif np.allclose(0,y2): root = b
  elif np.sign(y1) == np.sign(y2): # Check the signs of y are different   
    print("No root here") # If the signs of y1 and y2 are the same halt
  else:
    for i in steps: # steps for the interval of a and b
      int1 = a+i # interval 'a' will become 'int1'
      int2 = b+i # interval 'b' will become 'int2'
      for pos in range(0,100):
        c = int2 - (f(int2)*(int2-int1))/(f(int2)-f(int1)) ##false root # Calculate the value of c and f(c)
        if np.allclose(0,f(c), h): # If f(c) approaches 0, halt and obtain the root
          roots.append(c)
          break
        if np.sign(f(int1)) != np.sign(f(c)): int2,y2 = c,f(c) # If f(c) and f(int1) have opposite signs 
        else: int1,y1 = c,f(c) # set int1=c and y1=f(c)
  if roots is not None:
    return roots, pos


# In[ ]:


### Secant Method
def secant(f, a, b, steps, epochs = 100):
  roots = [] # list of roots 
  for i in steps: # steps for the interval of a and b
    intval1 = a+i # interval 'a' will become 'intval1'
    intval2 = b+i # interval 'b' will become 'intval2'
    for epoch in range(epochs):
      c = intval2 - (f(intval2)*(intval2-intval1))/(f(intval2)-f(intval1)) # Calculate for c
      if np.allclose(intval2,c): # If $x_2-x_1 approx 0, halt and retrieve root
        roots.append(c)
        break
      else:
        intval1,intval2 = intval2,c # Else intval1 = intval2 and intval2 = c
  return roots, epochs

