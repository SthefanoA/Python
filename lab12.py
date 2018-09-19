#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 11 16:46:13 2017

@author: Brandon_Garry, Garry, Brandon
"""

#lab12.py

import numpy as np
import matplotlib.pyplot as plt

def approx1(x):
    i = 1
    s = 0
    while i<=x:
        s = s+ (1/(i*(i+1)))
        i = i+1
    return s

def myln(n):
    i = 1
    s = 0
    while i<=n:
        s = s + ((-1)**(i-1))/i
        i = i+1
    return s

def mypi(n):
    i = 1
    s = 0
    while i<=n:
        s = s + (((-1)**(i-1))*(4))/(2*i-1)
        i = i + 1
    return s

def myex(x,n):
    i = 0
    s = 0
    while i<n:
        s = s + (x**(i))/(np.math.factorial(i))
        i = i + 1
    return s

def mysin(x,n):
    i = 0
    s = 0
    while i<n:
        s = s + ((-1)**i)*(x**(2*i+1))/(np.math.factorial(2*i+1))
        i = i + 1
    return s
    
fm = "{:0.8f} (exact) {:0.8f} (approx) {:0.8f} (diff)"
fm1 = "{:0.15f} (exact) {:0.15f} (approx) {:0.15f} (diff)"

#p01
p01a = approx1(10)
print('p01a =')
print(fm.format(1.0,p01a,1.0-p01a))
p01b = approx1(100)
print('p01b =')
print(fm.format(1.0,p01b,1.0-p01b))
fig, ax = plt.subplots()
i = 0
x = np.arange(1,51,dtype=np.float)
y = np.empty(50,dtype=np.float)
while i < 50:
    y[i]=approx1(i+1)
    i = i + 1
ax.plot(x,y)
ax.set_title('My series of approximation of 1')
ax.set_xlim(0,50)
ax.set_ylim(.4,1.0)


#p02
p02a = myln(10)
print('p02a =')
print(fm.format(np.log(2),p02a,np.log(2)-p02a))
p02b = myln(50)
print('p02b =')
print(fm.format(np.log(2),p02b,np.log(2)-p02b))
fig, ax = plt.subplots()
i = 0
x = np.arange(1,51,dtype=np.float)
y = np.empty(50,dtype=np.float)
while i<50:
    y[i] = myln(i+1)
    i = i + 1
ax.plot(x,y)
ax.set_title('My series approximation of ln2\nBrandon Garry')
ax.set_xlim(0,50)
ax.set_ylim(.4,1.0)


#p03
p03a = mypi(10)
print('p03a =')
print(fm.format(np.pi,p03a,np.pi-p03a))
p03b = mypi(50)
print('p03b =')
print(fm.format(np.pi,p03b,np.pi-p03b))
fig, ax = plt.subplots()
x = np.arange(1,51,dtype=np.float)
y = np.empty(50,dtype=np.float)
i = 0
while i<50:
    y[i] = mypi(i+1)
    i = i + 1
ax.plot(x,y)
ax.set_title('My series approximation of pi\nBrandon Garry')
ax.set_xlim(0,50)
ax.set_ylim(2.6,4.0)



#p04
p04a = myex(4.0,5)
print('p04a =')
print(fm.format(np.exp(4),p04a,np.exp(4)-p04a))
p04b = myex(4.0,20)
print('p04b =')
print(fm.format(np.exp(4),p04b,np.exp(4)-p04b))
fig, ax = plt.subplots()
i = 0
x = np.arange(1,21,dtype=np.float)
y = np.empty(20,dtype=np.float)
while i<20:
    y[i] = myex(4.0,i+1)
    i = i+1
ax.plot(x,y)
ax.set_title('my series approximation of e^4\nBrandon Garry')
ax.set_xlim(0,20)
ax.set_ylim(0,60)



#p05
p05a = mysin(np.pi/4.0,5)
print('p05a =')
print(fm1.format(np.sin(np.pi/4),p05a,np.abs(np.sin(np.pi/4)-p05a)))
p05b = mysin(np.pi/4.0,10)
print('p05b =')
print(fm1.format(np.sin(np.pi/4),p05b,np.abs(np.sin(np.pi/4)-p05b)))
fig, ax = plt.subplots()
i = 0
x = np.arange(1,11,dtype=np.float)
y = np.empty(10,dtype=np.float)
while i<10:
    y[i] = mysin(np.pi/4.0,i+1)
    i = i+1
ax.plot(x,y)
ax.set_title('my series approximation of sin(pi/4)\nBrandon Garry')
ax.set_xlim(1,10)
ax.set_ylim(.70,.79)
del x, y, i

del ax, fig, fm, fm1, plt