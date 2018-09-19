#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 13:11:15 2017

@author: Brandon_Garry, Garry, Brandon
"""

#lab05.py

import numpy as np

np.set_printoptions(threshold=np.nan,
    formatter = {'float_kind': lambda value: format(value, '8.4f'),
                    'int_kind': lambda value: format(value, '4d')})
#FINISHED
#p01
x = np.arange(1,11,1,dtype=np.int)
p01 = np.array([x,x*2])
print('p01. =')
print(p01)
del x

#p02
x = np.arange(10,0,-1,dtype=np.int)
p02 = np.array([x,x*10])
print('p02. = ')
print(p02)
del x

#p03
x = np.arange(1,20,2,dtype=np.int)
p03 = np.array([x,x**2])
print('p03. = ')
print(p03)
del x

#p04
x = np.arange(0,10,1,dtype=np.int)
p04 = np.array([x,x**2]).T
print('p04. =')
print(p04)
del x

#p05
x = np.arange(0,100,10,dtype=np.float)
p05 = np.array([x,np.sin(np.deg2rad(x))]).T.reshape(10,2)
print('p05. =')
print(p05)
del x

#p06
x = np.arange(0,10,1,dtype=np.float)
p06 = np.array([x,x*np.exp(-x)]).T.reshape(10,2)
print('p06. =')
print(p06)
del x

np.set_printoptions(threshold=np.nan,
    formatter = {'float_kind': lambda value: format(value, '8.2f'),
                    'int_kind': lambda value: format(value, '2d')})

#p07
x = np.arange(2,7,.5,dtype=np.float)
p07 = np.array([x,(10000)*((1+(x/100))**10)]).T.reshape(10,2)
print('p07. =')
print(p07)
del x

np.set_printoptions(threshold=np.nan,
    formatter = {'float_kind': lambda value: format(value, '9.4f'),
                    'int_kind': lambda value: format(value, '2d')})

#p08
x = np.arange(0,44,2,dtype=np.float)
a = 34172
b = 7.9622
p08 = np.array([x,(10**(b-((.05223*a)/(x+273.15))))]).T
print('p08. =')
print(p08)
del x, a, b

#p09
x = np.arange(1,9,1,dtype=np.float)
g = 9.81
h = 2
v = (np.sqrt(2*h*g))
t =((v/g)*(.85**x))
p09 = np.array([x,t]).T
print('p09. =')
print(p09)
del x, g, h, v

#p10
t = np.arange(1,32,5,dtype=np.int)
a = np.deg2rad(70)
g = 9.81
v = 162
x = v*t*(np.cos(a))
y = (v*t*np.sin(a))-((1/2)*g*(t**2))
r = np.sqrt((x**2)+(y**2))
tan = np.arctan(y/x)
p10 = np.array([r,np.rad2deg(tan)]).T
print('p10. =')
print(p10)
del t, a, g, v, x, y, r, tan

np.set_printoptions(threshold=np.nan,
    formatter = {'float_kind': lambda value: format(value, '8.2f'),
                    'int_kind': lambda value: format(value, '2d')})

#p11
r = .0485
p = 100000
y = np.arange(10,31,1,dtype=np.float)
m = (p*r/12)/(1-((1+(r/12))**(-12*y)))
t = 12*m*y
p11 = np.array([y,m,t]).T
print('p11. =')
print(p11)
del r, p, y, m, t

np.set_printoptions(threshold=np.nan,
    formatter = {'float_kind': lambda value: format(value, '8.4f'),
                    'int_kind': lambda value: format(value, '2d')})

#p12
k = np.arange(.2,.9,.1,dtype=np.float)
b = (((32000)/(np.pi**2))*((1/(1+k))*(1/((1-k)**2))))**(1/3)
a = (k*b)
s = (np.pi**2)*((b**2)-(a**2))
p12 = np.array([a,b,s]).T
print('p12. =')
print(p12)
del k, b, a, s

del np
