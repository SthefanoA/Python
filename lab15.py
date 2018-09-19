#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 21:51:45 2017

@author: Brandon_Garry, Garry, Brandon
"""

#lab15.py

import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt

np.set_printoptions(threshold=np.nan,
            formatter={'float_kind': lambda value: format(value, '0.10f'),
                       'int_kind': lambda value: format(value, '3d')})

def myfun1(x):
    return x*np.cos(x-4) + .5

def myfun2(x):
    return -myfun1(x)

x = np.linspace(0,2*np.pi,100)
y = myfun1(x)
fig, ax = plt.subplots()

#ROOTS
r = optimize.fsolve(myfun1,.5)
x0 = r[0]
y0 = myfun1(x0)
t0 = "({:0.2f},{:0.2f})".format(x0,y0)
r = optimize.fsolve(myfun1,2)
x1 = r[0]
y1 = myfun1(x1)
t1 = "({:0.2f},{:0.2f})".format(x1,y1)
r = optimize.fsolve(myfun1,5.5)
x2 = r[0]
y2 = myfun1(x2)
t2 = "({:0.2f},{:0.2f})".format(x2,y2)
ax = plt.scatter(x0,y0,s=40,facecolors='none',edgecolors='red',marker='o')
ax = plt.text(x0+.2,y0-.1,t0)
ax = plt.scatter(x1,y1,s=40,facecolors='none',edgecolors='red',marker='o')
ax = plt.text(x1+.2,y1-.1,t1)
ax = plt.scatter(x2,y2,s=40,facecolors='none',edgecolors='red',marker='o')
ax = plt.text(x2-1.2,y2-.1,t2)

#MIN
r = optimize.fmin(myfun1,1.5)
xmin = r[0]
ymin = myfun1(xmin)
tmin = "({:0.2f},{:0.2f})".format(xmin,ymin)
ax = plt.scatter(xmin,ymin,s=40,facecolors='none',edgecolors='red',marker='o')
ax = plt.text(xmin+.2,ymin-.5,tmin)

#MAX
r = optimize.fmin(myfun2,4)
xmax = r[0]
ymax = myfun1(xmax)
tmax = "({:0.2f},{:0.2f})".format(xmax,ymax)
ax = plt.scatter(xmax,ymax,s=40,facecolors='none',edgecolors='red',marker='o')
ax = plt.text(xmax+.2,ymax,tmax)

ax = plt.plot(x,y,color='blue')
ax = plt.grid(True,which='both',linestyle='--')
ax = plt.xticks(np.arange(0,7,1))
ax = plt.yticks(np.arange(-3,7,1))
ax = plt.xlim(0,6.3)
ax = plt.ylim(-3,6)
ax = plt.title('Brandon Garry\nMinima, maxima, and roots',fontsize=18)
ax = plt.xlabel('Y-Axis')
