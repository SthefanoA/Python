#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 14:10:34 2017

@author: Brandon_Garry, Garry, Brandon
"""

#lab03.py

import numpy as np

np.set_printoptions(threshold=np.nan,
            formatter={'float_kind': lambda value: format(value, '7.4f'),
                      'int_kind': lambda value: format(value, '4d')})

#p01
p01 = np.array([5.2**(3/2),(6.71)*(10**3),(3 + (5.1**2))*(np.cos(np.deg2rad(53))),15.8,90**(1/3),(np.sin(np.pi/3))/(np.tan(np.deg2rad(20)))])
print('p01 =')
print(p01)

#p02
p02 = np.array([(2.1)*(1/(10**(2))),(np.sin(1.7*np.pi)),28.5,2.7**(4/3),np.exp(3)]).reshape(5,1)
print('p02 =')
print(p02)

#p03
p03 = np.array([.75*(5.2**.7),11.1,60**(1/3),np.tan(10*np.pi/11),(np.cos(np.deg2rad(5)))**2,.116]).reshape(6,1)
print('p03 =')
print(p03)

#04
p04 = np.arange(0,11,1)
print('p04 = ')
print(p04)

#p05
p05 = np.arange(-5,6,1)
print('p05 =')
print(p05)

#p06
p06 = np.arange(0,1001,100).reshape(11,1)
print('p06 = ')
print(p06)

#p07
p07 = np.arange(3,27,3)
print('p07 =')
print(p07)

#p08
p08 = np.arange(68,4,-8, dtype='float').reshape(8,1)
print('p08 = ')
print(p08)

#p09
p09 = np.arange(6.4,12.1,.8, dtype='float').reshape(8,1)
print('p09 =')
print(p09)

#p10
p10 = np.linspace(7,7,9, dtype='int')
print('p10 =')
print(p10)

#p11
a = np.arange(1,9,1)
b = np.arange(7,0,-1)
p11 = np.append([a],[b])
print('p11. ')
print(p11)
del a,b

#p12
p12a = np.arange(0,30,5)
p12b = np.arange(600,0,-100)
p12c = np.arange(0,6,1)
p12 = np.append(np.append(p12a,p12b),p12c).reshape(3,6)
print('p12. ')
print(p12)
del p12a, p12b, p12c

#p13
p13a = np.arange(1,6,1, dtype='float')
p13b = np.linspace(0,0,5,dtype='float')
p13c = np.linspace(3,3,5,dtype='float')
p13 = np.array([p13a,p13b,p13c]).reshape(3,5)
print('p13. ')
print(p13)
del p13a, p13b, p13c

#p14
p14a = np.ones((1,4))
p14b = np.ones((1,4))
p14c = np.zeros((1,4))
p14d = np.ones((1,4))
p14 = np.array([p14a,p14b,p14c,p14d]).reshape(4,4)
print('p14. ')
print(p14)
del p14a, p14b, p14c, p14d

#p15
p15 = np.diag(np.array([1,2,3,4]))
print('p15. ')
print(p15)

p16 = np.ones((2,3))
print(p16)

del np

