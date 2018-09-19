#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 13:35:28 2017

@author: Brandon_Garry, Garry, Brandon
"""
#FINSIHED
#lab08.py

import numpy as np
import matplotlib.pyplot as plt

#p01
x = np.linspace(-3,5,100)
y = ((x+5)**2)/((4+3*(x)**2))
fig, ax = plt.subplots()
ax.plot(x,y,color='blue')
ax.set_title('p01')
ax.set_xlabel('x-axis')
ax.set_ylabel('y-axis')
ax.set_xlim(-3,5)
ax.set_ylim(0,7)

#p02
x = np.linspace(-5,10,100)
y = (5*(np.sin(x)))/(x + (np.exp(-.75*x))) - (3*x/5)
fig,ax = plt.subplots()
ax.plot(x,y,color='blue')
ax.set_title('p02')
ax.set_xlabel('x-axis')
ax.set_ylabel('y-axis')
ax.set_xlim(-6,10)
ax.set_ylim(-8,4)

#p03
x = np.linspace(-2,2,200)
y = np.sqrt(np.absolute(np.cos(3*x))) + (np.sin(4*x))**2
fig,ax = plt.subplots()
ax.plot(x,y,color='blue')
ax.set_title('p03')
ax.set_xlabel('x-axis')
ax.set_ylabel('y-axis')
ax.set_xlim(-2.0,2.0)
ax.set_ylim(0.0,2.0)

#p04
x = np.linspace(-20,30,200)
y = 5*(np.exp(2*np.sin(.4*x)))*(np.cos(4*x))
fig, ax = plt.subplots()
ax.plot(x,y,color='blue')
ax.set_title('p04')
ax.set_xlabel('x-axis')
ax.set_ylabel('y-axis')
ax.set_xlim(-20,30)
ax.set_ylim(-40,40)

#p05
x1 = np.linspace(-4,-1.1,100)
x2 = np.linspace(-.9,3,100)
y1 = (x1**2 + 3*x1 +3)/(.8*(x1+1))
y2 = (x2**2 + 3*x2 +3)/(.8*(x2+1))
fig, ax = plt.subplots()
ax.plot(x1,y1,color='blue')
ax.plot(x2,y2,color='green',linestyle='--')
ax.set_title('p05')
ax.set_xlabel('x-axis')
ax.set_ylabel('y-axis')
ax.set_xlim(-4,3)
ax.set_ylim(-15,15)

#p06
t1 = np.linspace(-30,-1.6,1000)
t2 = np.linspace(-.6,40,1000)
x1 = (3*t1)/(1+(t1**3))
y1 =(3*(t1**2))/(1+(t1**3))
x2 = (3*t2)/(1+(t2**3))
y2 = (3*(t2**2))/(1+(t2**3))
fig, ax = plt.subplots()
ax.plot(x1,y1,color='blue')
ax.plot(x2,y2,color='green',linestyle='--')
ax.set_title('p06')
ax.set_xlabel('x-axis')
ax.set_ylabel('y-axis')
ax.set_xlim(-2.0,2.0)
ax.set_ylim(-2.5,2.0)

#P07
x = np.linspace(-300,300,1000)
y = 693.8 - (68.8*np.cosh(x/99.7))
fig, ax = plt.subplots()
ax.plot(x,y,color='blue')
ax.set_title('p07')
ax.set_xlabel('x-axis')
ax.set_ylabel('y-axis')
ax.set_xlim(-300,300)
ax.set_ylim(-100,700)

del x, y, ax, fig
