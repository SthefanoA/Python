#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 13:18:50 2017

@author: Brandon_Garry, Garry, Brandon
"""
#FINSIHED
#lab06.py

import numpy as np

np.set_printoptions(threshold=np.nan,
            formatter={'float_kind' : lambda value: format(value,'7.4f'),
                       'int_kind' :   lambda value: format(value,'4d')})

fm = "{:0.4f}"

np.random.seed(1)

#p01
p01a = np.random.randint(0,10,[10])
print('p01a =')
print(p01a)
p01b = np.min(p01a)
print('p01b =')
print(p01b)
p01c = np.max(p01a)
print('p01c =')
print(p01c)

#p02
p02a = np.random.randint(0,100,[10])
print('p02a =')
print(p02a)
p02b = np.min(p02a)
print('p02b =')
print(p02b)
p02c = np.max(p02a)
print('p02c =')
print(p02c)
p02d = np.average(p02a)
print('p02d =')
print(p02d)

#p03
p03a = np.random.randint(10,20,[10])
p03b = np.sum(p03a)
print('p03a =')
print(p03a)
print('p03b =')
print(p03b)

np.random.seed(1)

#p04
p04a = np.random.randint(1,11,[10])
p04b = np.prod(p04a)
print('p04a =')
print(p04a)
print('p04b =')
print(p04b)

#p05
p05a = np.random.randint(1,11,size=[2,10])
p05b = np.sum(p05a)
print('p05a =')
print(p05a)
print('p05b =')
print(p05b)

#p06
p06a = np.random.randint(1,5,size=[5,2])
p06b = np.sum(p06a)
p06c = np.prod(p06a)
print('p06a =')
print(p06a)
print('p06b =')
print(p06b)
print('p06c =')
print(p06c)

#p07
p07a = np.random.randint(1,5,5)
p07b = np.random.randint(1,5,5)
p07c = np.array(p07a*p07b)
p07d = np.sum(p07c)
print('p07a =')
print(p07a)
print('p07b =')
print(p07b)
print('p07c =')
print(p07c)
print('p07d =')
print(p07d)

#p08
p08a = np.random.randint(1,5,5)
p08b = np.sum(p08a**2)
print('p08a =')
print(p08a)
print('p08b =')
print(p08b)

np.random.seed(1)

#p09
p09a = np.random.rand(10)*100
p09b = np.array([np.average(p09a)],dtype=np.float)
print('p09a =')
print(p09a)
print('p09b =')
print(p09b)

#p10
p10a = np.random.rand(10)*20-10
p10b = np.min(p10a)
p10c = np.max(p10a)
print('p10a =')
print(p10a)
print('p10b =')
print(fm.format(p10b))
print('p10c =')
print(fm.format(p10c))

#p11
p11a = np.random.rand(4,5)*100
p11b = np.sum(p11a)
print('p11a =')
print(p11a)
print('p11b = ')
print(fm.format(p11b))

np.set_printoptions(threshold=np.nan,
            formatter={'float_kind' : lambda value: format(value,'8.4f'),
                       'int_kind' :   lambda value: format(value,'4d')})

#p12
p12a = np.random.rand(2,5)*200-100
p12b = np.array([p12a]).T.reshape(5,2)
print('p12a =')
print(p12a)
print('p12b =')
print(p12b)

del fm, np