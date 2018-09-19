#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  3 14:02:03 2017

@author: Brandon_Garry, Garry, Brandon
"""

#lab10.py

import numpy as np
import matplotlib.pyplot as plt

fm = '{:0.2f}'

#p01
x = np.arange(0,6,1)
y = np.array([0,20,60,68,77,110])
p01 = np.array([x,y])
print('p01 =')
print(p01)

#p02
def sum(a):
    i=0
    n=len(a)
    s=0
    while i < n:
        s = s+a[i]
        i = i +1
    return s

p02 = sum(x)
print('p02 =')
print(p02)

#p03
p03 = sum(y)
print('p03= ')
print(p03)

#p04
def sumprod(a,b):
    i=0
    n=len(a)
    s=0
    while i < n:
        s = s + (a[i]*b[i])
        i = i+1
    return s

p04 = sumprod(x,x)
print('p04 =')
print(p04)

#p05
p05 = sumprod(x,y)
print('p05= ')
print(p05)

#p06
def ave(a):
    s = sum(a)
    n = len(a)
    return s/n

p06 = ave(x)
print('p06 =')
print(fm.format(p06))

#p07
p07 = ave(y)
print('p07 =')
print(fm.format(p07))

#p08
def m(a,b):
    n = len(a)
    return ((sumprod(a,b))-((sum(a)*sum(b)))/n)/((sumprod(x,x))-((sum(x)**2)/n))

def b(x,y):
    return ave(y) - m(x,y)*ave(x)

fm1 = "y = {:0.2f}x + {:0.2f}"
p08 = fm1.format(m(x,y),b(x,y))
print('p08 =')
print(p08)

#p09

def yfit(x,y):
    return np.linspace(b(x,y),5*m(x,y),6)


fig, ax = plt.subplots()
ax.set_title("Least Squares Fitted Line\nBrandon Garry")
ax.scatter(x,y, s=40, facecolors = "none", edgecolors = "red", marker='o')
ax.plot(x,yfit(x,y), color="blue", linestyle='--')
ax.legend(["xyfit", "xydata"], loc='center right')
ax.set_xlim([-1,6])
ax.set_ylim([-20,120])

del ax, fig, fm, fm1, plt

    
    
