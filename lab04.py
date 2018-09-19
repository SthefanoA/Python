#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 13:18:56 2017

@author: Brandon_Garry, Garry, Brandon
"""

#lab4.py

import numpy as np

np.set_printoptions(threshold=np.nan,
        formatter = {'float_kind': lambda value: format(value,'0.4f'),
                       'int_kind': lambda value: format(value,'1d')})
#FINISHED
#p01
x = np.arange(-2,5,1,dtype=np.int)
y = x**3 - 2*(x**2) + x
p01 = y
print('p01 =')
print(p01)
del x,y

#p02
x = np.arange(1,8,1,dtype=np.float)
y = (x-3)*((x**2)+3)/(x**2)
p02 = y
print('p02 =')
print(p02)
del x, y

#p03
v = np.arange(2,12,2,dtype=np.float)
y = (1/v)
p03a = y
print('p03a =')
print(p03a)
del y
y = (1/(v**2))
p03b = y
print('p03b =')
print(p03b)
del y
y = (v/2)
p03c = y
print('p03c =')
print(p03c)
del y
y = (v/v)
p03d = y
print('p03d =')
print(p03d)
del y,v

#p04
v = np.arange(5,0,-1,dtype=np.int)
y = (v**2)
p04a = y
print('p04a =')
print(p04a)
del y
y = (v**v)
p04b = y
print('p04b =')
print(p04b)
del y
y = (v*5)
p04c = y
print('p04c =')
print(p04c)
del y
y = (v-1)
p04d = y
print('p04d =')
print(p04d)
del y,v

np.set_printoptions(threshold=np.nan,
        formatter = {'float_kind': lambda value: format(value,'0.0f'),
                       'int_kind': lambda value: format(value,'4d')})

#p05
x = np.arange(0,110,10,dtype=np.int)
y = (x*(9/5)) + 32
p05 = y
print('p05 =')
print(p05)
del x,y

np.set_printoptions(threshold=np.nan,
        formatter = {'float_kind': lambda value: format(value,'0.4f'),
                       'int_kind': lambda value: format(value,'4d')})

#p06
x = np.arange(0,91,15,dtype=np.int)
y = np.sin(np.deg2rad(x))
p06 = y
print('p06 =')
print(p06)
del x,y

np.set_printoptions(threshold=np.nan,
        formatter = {'float_kind': lambda value: format(value,'0.0f'),
                       'int_kind': lambda value: format(value,'1d')})

#p07
x = np.arange(1,11,1,dtype=np.int)
y = ((-1)**(x+1))
p07 = y
print('p07 =')
print(p07)
del x,y

np.set_printoptions(threshold=np.nan,
        formatter = {'float_kind': lambda value: format(value,'0.3f'),
                       'int_kind': lambda value: format(value,'4d')})

#p08
x = np.arange(1,11,1,dtype=np.int)
y = (((-1)**(x+1))/(x))
p08 = y
print('p08 = ')
print(p08)
del x,y

np.set_printoptions(threshold=np.nan,
        formatter = {'float_kind': lambda value: format(value,'0.0f'),
                       'int_kind': lambda value: format(value,'4d')})

#p09
n = np.arange(1,11,1,dtype=np.int)
y = (n*(n+1))/2
p09 = y
print('p09 =')
print(p09)
del n,y

np.set_printoptions(threshold=np.nan,
        formatter = {'float_kind': lambda value: format(value,'0.0f'),
                       'int_kind': lambda value: format(value,'0d')})

#p10
n = np.arange(1,11,1,dtype=np.int)
y = (n**n)
p10 = y
print('p10 =')
print(p10)
del n,y

del np