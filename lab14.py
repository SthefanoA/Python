#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 24 15:45:37 2017

@author: Brandon_Garry, Garry, Brandon
"""

#lab14.py

import numpy as np
import matplotlib.pyplot as plt

np.set_printoptions(threshold=np.nan,
            formatter={'float_kind':lambda value:format(value, '0.10f'),
                       'int_kind':lambda value:format(value, '3d')})


#P01
x = np.arange(6,dtype=np.float)
y = np.array([0.0,.8,.9,.1,-.8,-1.0])

p1 = np.polyfit(x,y,1)
p2 = np.polyfit(x,y,2)
p3 = np.polyfit(x,y,5)
p4 = np.polyfit(x,y,20)

xfit = np.linspace(x[0],x[len(x)-1],100)
yfit1 = np.polyval(p1,xfit)
yfit2 = np.polyval(p2,xfit)
yfit3 = np.polyval(p3,xfit)
yfit4 = np.polyval(p4,xfit)

fig = plt.figure()
plt.subplot(2,2,1)
plt.scatter(x,y,s=40,facecolors='none',edgecolors='green',marker='o')
plt.plot(xfit,yfit1,'-')
plt.legend(['deg1','raw'],loc='upper right',fontsize='small')
plt.xlim(-1,6)
plt.ylim(-1.5,1.5)
plt.xticks(np.arange(-1,7,1))
plt.yticks(np.arange(-1.5,1.6,.5))
plt.title('Deg1',fontsize=8)

plt.subplot(2,2,2)
plt.scatter(x,y,s=40,facecolors='none',edgecolors='green',marker='o')
plt.plot(xfit,yfit2,'-')
plt.legend(['deg2','raw'],loc='upper right',fontsize='small')
plt.xlim(-1,6)
plt.ylim(-1.5,1.5)
plt.xticks(np.arange(-1,7,1))
plt.yticks(np.arange(-1.5,1.6,.5))
plt.title('Deg2',fontsize=8)

plt.subplot(2,2,3)
plt.scatter(x,y,s=40,facecolors='none',edgecolors='green',marker='o')
plt.plot(xfit,yfit3,'-')
plt.legend(['deg5','raw'],loc='upper right',fontsize='small')
plt.xlim(-1,6)
plt.ylim(-1.5,1.5)
plt.xticks(np.arange(-1,7,1))
plt.yticks(np.arange(-1.5,1.6,.5))
plt.title('Deg5',fontsize=8)

plt.subplot(2,2,4)
plt.scatter(x,y,s=40,facecolors='none',edgecolors='green',marker='o')
plt.plot(xfit,yfit4,'-')
plt.legend(['deg20','raw'],loc='upper right',fontsize='small')
plt.xlim(-1,6)
plt.ylim(-1.5,1.5)
plt.xticks(np.arange(-1,7,1))
plt.yticks(np.arange(-1.5,1.6,.5))
plt.title('Deg20',fontsize=8)

fig.suptitle('My Title\nBrandon Garry',fontsize=16)
fig.tight_layout()
fig.subplots_adjust(top=0.8)

#P02
p02a = np.array([0.2,-1.25],dtype=np.float)
p02b = np.array([0.14,-3],dtype=np.float)
p02c = np.array([0.12,-2],dtype=np.float)
p02d = np.array([0.1,-1],dtype=np.float)
p02 = np.convolve(np.convolve(p02a,p02b),np.convolve(p02c,p02d))
x = np.linspace(5,23,80)
y = np.polyval(p02,x)
xr = np.roots(p02)
yr = np.polyval(p02,xr)

fix, ax = plt.subplots()
ax = plt.plot(x,y,color='blue')
ax = plt.scatter(xr,yr, s=50, facecolors='none',edgecolors='r',marker='o')
ax = plt.title('Brandon Garry',fontsize=16)
ax = plt.legend(['polynomial','roots'],loc='upper right')
ax = plt.xlim(5,23)
ax = plt.ylim(-.4,.8)
ax = plt.xticks(np.arange(5,23.1,2))
ax = plt.yticks(np.arange(-.4,.9,.2))
ax = plt.ylabel('y-axis')
ax = plt.xlabel('x-axis')

