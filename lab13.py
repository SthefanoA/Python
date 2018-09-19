#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 22 15:15:59 2017

@author: Brandon_Garry, Garry, Brandon
"""

#lab13.py

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

np.set_printoptions(threshold=np.nan,
            formatter={'float_kind':lambda value:format(value,'3.0f'),
                       'int_kind':lambda value: format(value,'3d')})

#p01
p01 = np.array([-.4,0,7,-20.5,-28],dtype=np.float)
x = np.linspace(-5,5,40)
y = np.polyval(p01,x)
fig, ax = plt.subplots()
ax.plot(x,y,color='blue')
ax.set_xlabel('x-axis')
ax.set_ylabel('y-axis')
ax.set_title('Brandon Garry')
ax.set_xticks(np.arange(-5,5,1.5))
ax.set_yticks(np.arange(-120,81,20))
ax.set_ylim(-120,80)
ax.set_xlim(-5,4)
plt.show()

#p02
p02 = np.array([-.001,.051,-.76,3.8,-1.4],dtype=np.float)
x = np.linspace(1,14.1,40)
y = np.polyval(p02,x)
fig, ax = plt.subplots()
ax.plot(x,y,color='blue')
ax.set_xlabel('x-axis')
ax.set_ylabel('y-axis')
ax.set_title('Brandon Garry')
ax.set_xticks(np.arange(1,14.5,1))
ax.set_yticks(np.arange(1,5.1,.5))
ax.set_ylim(1,5)
ax.set_xlim(1,14)
plt.show()

#p03
p03a = np.array([1,1.4],dtype=np.float)
p03b = np.array([1,-.4],dtype=np.float)
p03c = np.array([1,.6],dtype=np.float)
p03d = np.array([1,-1.4],dtype=np.float)
p03 = np.convolve(np.convolve(p03a,p03b),np.convolve(p03c,p03d))
x = np.linspace(-1.5,1.5,40)
y = np.polyval(p03,x)
fig, ax = plt.subplots()
ax.plot(x,y,color='blue')
ax.set_xlabel('x-axis')
ax.set_ylabel('y-axis')
ax.set_title('Brandon Garry')
ax.set_xticks(np.arange(-1.5,1.6,.5))
ax.set_yticks(np.arange(-1,1.1,.2))
ax.set_ylim(-1,1)
ax.set_xlim(-1.5,1.5)
plt.show()

#p04
p04a = np.array([2,0,3],dtype=np.float)
p04b = np.array([1,3.5,5,-16],dtype=np.float)
p04 = np.convolve(p04a,p04b)
print('p04 =')
print(p04)
del p04a, p04b

#p05
p05a = np.array([-.6,0,7.7,-8,-24.6,48],dtype=np.float)
p05b = np.array([-.6,0,4.1,-8],dtype=np.float)
p05q, p05r = signal.deconvolve(p05a,p05b)
print('p05q =')
print(p05q)
print('p05r =')
print(p05r)
del p05a, p05b

#p06
p06a = np.array([1,-6,13,-12,4],dtype=np.float)
p06b = np.array([1,-3,2],dtype=np.float)
p06q, p06r = signal.deconvolve(p06a,p06b)
print('p06q =')
print(p06q)
print('p06r =')
print(p06r)
del p06a, p06b

#p07
p07a = np.array([1,0,0,0],dtype=np.float)
p07b = np.polyder(p07a)
p07c = np.polyder(p07b)
x = np.linspace(-2,2,40,dtype=np.float)
y = np.polyval(p07a,x)
y1 = np.polyval(p07b,x)
y2 = np.polyval(p07c,x)
fig, ax = plt.subplots()
ax.plot(x,y,color='blue')
ax.plot(x,y1,color='green')
ax.plot(x,y2,color='red')
ax.set_xticks(np.arange(-2,2.1,.5))
ax.set_yticks(np.arange(-15,16,5))
ax.set_ylim(-15,15)
ax.set_xlim(-2,2)
ax.legend(['y=x^3','y=3x^2','y=6x'],loc='lower right',fontsize='large')
ax.set_title('Brandon Garry')
plt.show()

#p08
p08a = np.array([.41,-10.8,64,-8.2,4.4],dtype=np.float)
p08b = np.polyder(p08a)
p08c = np.polyder(p08b)
x = np.linspace(0,8,40,dtype=np.float)
y = np.polyval(p08a,x)
y1 = np.polyval(p08b,x)
y2 = np.polyval(p08c,x)
plt.subplot(311)
plt.plot(x,y,'-',color='blue')
plt.title('Brandon Garry')
plt.xlim(0,8)
plt.ylim(-200,600)
plt.xticks(np.arange(0,9,1))
plt.yticks(np.arange(-200,700,200))
plt.ylabel('Pos(ft)')
plt.subplot(312)
plt.plot(x,y1,'-',color='blue')
plt.xlim(0,8)
plt.ylim(-400,200)
plt.xticks(np.arange(0,9,1))
plt.yticks(np.arange(-400,300,200))
plt.ylabel('Vel(ft/s)')
plt.subplot(313)
plt.plot(x,y2,'-',color='blue')
plt.xlabel('Time(s)')
plt.xlim(0,8)
plt.ylim(-200,200)
plt.xticks(np.arange(0,9,1))
plt.yticks(np.arange(-200,300,200))
plt.ylabel('Acc(ft/s^2)')
plt.subplots_adjust(hspace=.5)
plt.show()

del ax, fig, x, y, y1, y2, plt, signal
