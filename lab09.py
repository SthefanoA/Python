#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  1 14:04:08 2017

@author: Brandon_Garry, Garry, Brandon
"""

#lab09.py

import numpy as np

np.set_printoptions(threshold=np.nan,
            formatter= {'float_kind': lambda value: format(value, '8.4f'),
                        'int_kind': lambda value: format(value, '4d')})

def kmlTOmpg(kml):
    return kml* 2.35214

def problem2(x):
    return (-.2*(x**4)) + np.exp(-.5*x)*(x**3) + 7*(x**2)

def mphTOmps(mph):
    return mph * .44704

def triangle(a,b,c):
    s = (a+b+c)/2
    area = np.sqrt(s*(s-a)*(s-b)*(s-c))
    return area

def Triarea(a,b,c):
    ab = b-a
    ac = c-a
    c = np.cross(ab,ac)
    return c

def CartToPolar(x,y):
    rad = np.sqrt((x**2)+(y**2))
    o = np.arctan(y/x)
    d = np.rad2deg(o)
    if x>=0 and y>=0:
        th = d
    elif x>=0 and y<0:
        th = d
    elif x<0 and y>0:
        th = 180 + d
    else:
        th = -180 + d
    return np.array([th,rad])

def centroidT(w,h,t,d):
    a1 = (w*t)
    y1 = (h-t)+(t/2)
    a2 = ((h-t)*d)
    y2 =(h-t)/2
    yc = ((y1*a1)+(y2*a2))/(a1+a2)
    return yc

fm = '{:8.4f}'

#p01
p01 = kmlTOmpg(14)
print('p01 =')
print(fm.format((p01)))

#p02
x = np.arange(-3,5,1)
p02 = problem2(x)
print('p02= ')
print(p02)
del x

#p03
p03 = mphTOmps(55)
print('p03 =')
print(fm.format((p03)))

#p04
p04 = triangle(3,8,10)
print('p04 =')
print(fm.format((p04)))

#p05
a = np.array([-1.5, -4.2, -3])
b = np.array([-5.1, 6.3, 2])
c = np.array([12.1, 0, -.5])
v = Triarea(a,b,c)
p05 = np.sqrt(v[0]**2 + v[1]**2 + v[2]**2)/2
print('p05 =')
print(fm.format((p05)))
del a, b, c, v

np.set_printoptions(threshold=np.nan,
            formatter= {'float_kind': lambda value: format(value, '9.4f'),
                        'int_kind': lambda value: format(value, '4d')})

#p06
p06a = CartToPolar(14,9)
print('p06a =')
print(p06a)
p06b = CartToPolar(-11,-20)
print('p06b =')
print(p06b)
p06c = CartToPolar(-15,4)
print('p06c =')
print(p06c)
p06d = CartToPolar(13.5,-23.5)
print('p06d =')
print(p06d)

#p07
p07 = centroidT(240,380,60,42)
print('p07 =')
print(fm.format((p07)))

del fm