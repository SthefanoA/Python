#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 22:40:13 2017

@author: Brandon_Garry, Garry, Brandon
"""

#lab16.py

import numpy as np
from scipy import integrate
from scipy import misc
import matplotlib.pyplot as plt


#Problem 1
p = np.array([1,-12.4,40.59,-17.015,-71.95,35.88],dtype=np.float)
pd = np.polyder(p)
x = np.linspace(-2,7,100)
y = np.polyval(p,x)
y1 = np.polyval(pd,x)
fig, ax = plt.subplots()
ax.plot(x,y,color='b')
ax.plot(x,y1,color='g')
ax.set_xlim(-1.51,6.65)
ax.set_ylim(-600,600)
ax.set_title('Brandon Garry',fontsize=16)
ax.set_yticks(np.arange(-600,620,200))
ax.set_xticks(np.arange(-1,7,1))
ax.legend(['f','f^'],loc=9)
plt.show()

#Problem 2
def fun1(x):
    return x**2 + 4*np.sin(2*x) - 1

x = np.linspace(-3,3,100)
y = fun1(x)
y1 = misc.derivative(fun1,x,dx=0.001)
fig, ax = plt.subplots()
ax.plot(x,y,color='blue')
ax.plot(x,y1,color='g')
ax.set_xlim(-3,3)
ax.set_ylim(-15,15)
ax.set_title('Brandon Garry',fontsize=16)
ax.set_yticks(np.arange(-15,16,5))
ax.set_xticks(np.arange(-3,3.5,1))
ax.legend(['f','f^'],loc='lower right')

#Problem 3
def fun2(x):
    return x*np.sin(x)

x = np.linspace(0,np.pi,100)
y = fun2(x)
fig, ax = plt.subplots()
ax = plt.plot(x,y)
ax = plt.fill_between(x,y,0,color='b')
area = integrate.quad(fun2,0,np.pi)
area = area[0]
t = "Area = {:0.6f}".format(area)
ax = plt.text(1.2,.75,t,fontsize=16,color='w')
ax = plt.title('Brandon Garry',fontsize=16)
ax = plt.xlim(0,3.5)
ax = plt.ylim(0,2.0)
ax = plt.yticks(np.arange(0,2.1,.5))

#Problem 4
x = np.arange(0,13,1)
y = np.array([0,1,2,4,8,16,32,16,8,4,2,1,0],dtype=np.float)
area = integrate.trapz(y,x)
fig,ax = plt.subplots()
ax = plt.plot(x,y,color='b')
ax = plt.fill_between(x,y,0,color='g')
ax = plt.xlim(0,12)
ax = plt.ylim(0,35)
ax = plt.xticks(np.arange(0,14,2))
ax = plt.yticks(np.arange(0,36,5))
t = "Area = {:0.2f}".format(area)
ax = plt.text(4.25,4,t,fontsize=14,color='w')
ax = plt.title('Brandon Garry',fontsize=16)

#Problem 5
x = np.arange(0,10,1)
y1 = np.array([13.0,13.5,12.5,12.8,12.3,13.2,13.0,13.7,12.8,13.3],dtype=np.float)
y2 = np.array([8.0,6.3,6.0,6.5,7.1,7.8,7.2,6.8,7.3,7.0],dtype=np.float)
y3 = np.linspace(30,30,10)
area1 = integrate.trapz(y2,x)
area2 = integrate.trapz(y1,x)
fig,ax = plt.subplots()
ax = plt.plot(x,y1,color='r')
ax = plt.fill_between(x,y1,y2,color='g')
ax = plt.plot(x,y2,color='b')
ax = plt.fill_between(x,y2,0,color='b')
ax = plt.plot(x,y3,color='r')
ax = plt.fill_between(x,y3,y1,color='r')
ax = plt.ylim(0,18)
ax = plt.xlim(0,9)
ax = plt.yticks(np.arange(0,20,2))
ax = plt.xticks(np.arange(0,10,1))
ax = plt.title('Brandon Garry',fontsize=16)
t1 = "Area = {:0.2f}".format(area1)
t2 = "Area = {:0.2f}".format(area2-area1)
ax = plt.text(3,3,t1,fontsize=16,color='w')
ax = plt.text(3,10,t2,fontsize=16,color='w')

#Problem 6
def myfun6a(x):
    return np.sin(x) + 11.5

def myfun6b(x):
    return np.cos(2*x) + 6

x = np.linspace(0,4*np.pi,100)
y1 = myfun6a(x)
y2 = myfun6b(x)
y3 = np.linspace(100,100,100)
area1 = integrate.quad(myfun6a,0,4*np.pi)
area2 = integrate.quad(myfun6b,0,4*np.pi)
area1 = area1[0]
area2 = area2[0]
fig, ax = plt.subplots()
ax = plt.plot(x,y1,color='g')
ax = plt.plot(x,y2,color='k')
ax = plt.xlim(0,4*np.pi)
ax = plt.ylim(0,15)
ax = plt.fill_between(x,y2,0,color='k')
ax = plt.fill_between(x,y3,y1,color='b')
ax = plt.fill_between(x,y1,y2,color='g')
ax = plt.title('Brandon Garry',fontsize=16)
t1 = "Area = {:0.2f}".format(area1-area2)
t2 = "Area = {:0.2f}".format(area2)
ax = plt.text(4,8.5,t1,fontsize=16,color='w')
ax = plt.text(4,3,t2,fontsize=16,color='w')