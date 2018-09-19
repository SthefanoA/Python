#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  8 13:12:29 2017

@author: Brandon_Garry, Garry, Brandon
"""

#lab11.py

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def distance(x,y):
    i = 0
    n = len(x)
    s = 0.0
    while i < n-1:
        s = s + np.sqrt((x[i+1]-x[i])**2 + (y[i+1]-y[i])**2)
        i = i + 1
    return s

fm = '{:9.5f}'

#p01
n = 4
t = np.linspace(np.pi/2,2*np.pi+np.pi/2,n)
x = np.cos(t)
y = np.sin(t)
p01 = distance(x,y)/2
print('p01 =')
print(fm.format(p01))
fig, ax = plt.subplots()
ax.plot(x,y,color='blue',linestyle='-')
ax.set_title('Triangle\nBrandon Garry')
ax.axis('equal')
del n, x, y, t

#p02
n = 5
t = np.linspace(np.pi/2,2*np.pi+np.pi/2,n)
x = np.cos(t)
y = np.sin(t)
p02 = distance(x,y)/2
print('p02 =')
print(fm.format(p02))
fig, ax = plt.subplots()
ax.plot(x,y,color='blue',linestyle='-')
ax.set_title('Square\nBrandon Garry')
ax.axis('equal')
ax.set_xlim(-1.5,1.5)
ax.set_ylim(-1,1)

#p03
n = 8
t = np.linspace(np.pi/2,2*np.pi+np.pi/2,n)
x = np.cos(t)
y = np.sin(t)
p03 = distance(x,y)/2
print('p03 =')
print(fm.format(p03))
fig, ax = plt.subplots()
ax.plot(x,y,color='blue',linestyle='-')
ax.set_title('Polygon 7 Sides\nBrandon Garry')
ax.axis('equal')
ax.set_xlim(-1.5,1.5)
ax.set_ylim(-1,1)
ax.yaxis.tick_right()

#p04
n = 20
t = np.linspace(np.pi/2,2*np.pi+np.pi/2,n)
x = np.cos(t)
y = np.sin(t)
p04 = distance(x,y)/2
print('p04 =')
print(fm.format(p04))
fig, ax = plt.subplots()
ax.plot(x,y,color='blue',linestyle='-')
ax.set_title('Circle Approx #1\nBrandon Garry')
ax.axis('equal')
ax.set_xlim(-1.5,1.5)
ax.set_ylim(-1,1)

#p05
n = 1000
t = np.linspace(np.pi/2,2*np.pi+np.pi/2,n)
x = np.cos(t)
y = np.sin(t)
p05 = distance(x,y)/2
print('p05 =')
print(fm.format(p05))
fig, ax = plt.subplots()
ax.plot(x,y,color='blue',linestyle='-')
ax.set_title('Circle Approx #2\nBrandon Garry')
ax.axis('equal')
ax.set_xlim(-1.5,1.5)
ax.set_ylim(-1,1)
del n

#p06 HOW TO GET Y AXIS RIGHT
def distance3(x,y,z):
    i = 0
    n = len(x)
    s = 0.0
    while i < n-1:
        s = s + np.sqrt((x[i+1]-x[i])**2 + (y[i+1]-y[i])**2 + (z[i+1]-z[i])**2)
        i = i +1
    return s

t = np.linspace(0, 32*np.pi, 1024)
x = t*np.cos(t)
y = t*np.sin(t)
z = t * .05
p06 = distance3(x,y,z)
print('p06 =')
print(fm.format(p06))
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(x,y,z,color='blue',label='3DSpiral')
ax.set_title('3D Spiral\nBrandon Garry')
ax.legend()
ax.set_zlim([0,6])
ax.set_xlim([-100,150])
ax.set_ylim([-100,100])
del t,x,y,z

del ax, fig, fm, plt, Axes3d