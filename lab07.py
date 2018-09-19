#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 15:30:52 2017

@author: Brandon_Garry, Garry, Brandon
"""

#lab07.py

import numpy as np
import matplotlib.pyplot as plt

np.set_printoptions(threshold=np.nan,
    formatter = {'float_kind': lambda value: format(value, '0.0f'),
                    'int_kind': lambda value: format(value, '4d')})

tch = np.array([75,79,86,86,79,81,73,89,91,86,81,82,86,88,89,90,82,84,81,79,73,69,73,79,82,72,66,71,69,66,66])
tsf = np.array([69,68,70,73,72,71,69,76,85,87,74,84,76,68,79,75,68,68,73,72,79,68,68,69,71,70,89,95,90,66,69])

#p01
s = 0
i = 0
while i < len(tch):
     s = s + tch[i]
     i = i + 1
p01 = s/(len(tch))
print('p01 =')
print(p01)
del s, i

#p02
s = 0
i = 0
while i < len(tsf):
    s = s + tsf[i]
    i = i +1
p02 = s/(len(tsf))
print('p02 =')
print(p02)
del s, i

#p03
p03 = 0
i = 0
while i < len(tch):
    if tch[i] > p01:
        p03 = p03 + 1
    else:
        p03 = p03 + 0
    i = i + 1
print('p03 =')
print(p03)
del i

#p04
p04 = np.array([])
u = np.array([])
i = 0
while i < len(tsf):
    if tsf[i] > p02:
        p04 = np.hstack([p04,i+1])
    else:
        u = np.hstack([u,i+1])
    i = i + 1
print('p04 =')
print(p04)
del i, u

#p05 SHOW EVERYTHING
p05 = np.array([])
u = np.array([])
i = 0
while i < len(tsf):
    if tsf[i] < tch[i]:
        p05 = np.hstack([p05,i+1])
    else:
        u = np.hstack([u,i+1])
    i = i + 1
print('p05 =')
print(p05)
del i, u

#p06
p06 = np.array([])
u = np.array([])
i = 0
while i < len(tsf):
    if tsf[i] == tch[i]:
        p06 = np.hstack([p06,i+1])
    else:
        u = np.hstack([u,i+1])
    i = i + 1
print('p06 =')
print(p06)
del i, u

#p07
bins = np.linspace(1,len(tsf),len(tsf))
fig, ax = plt.subplots()
ax.bar(bins,tch,1,color='red',edgecolor='black')
ax.bar(bins,tsf,1,color='purple',edgecolor='black')
ax.legend(['TCH','TSF'], loc='upper right')
ax.set_ylabel('Temperatures (F˚)')
ax.set_xlabel('August')
ax.set_title('P07')
ax.set_xlim(0,35)
ax.set_ylim(0,100)
del ax, bins, fig

#p08
i = 0
s = 0
while i <= 10:
    s = s+ (np.sqrt(12))*(((-1)/3)**i)/((2*i)+1)
    i = i + 1
p08 = s
print('p08 =')
print(p08)
del i, s

fm = "{:8.16f}"

#p09
i = 0
s = 0
d = np.deg2rad(45)
while i <= 10:
    s = s + ((-1)**i)*(d**((2*i)+1))/(np.math.factorial((2*i)+1))
    i = i +1
p09 = s
print('p09 =')
print(fm.format(p09))
del i, s, d

del np, plt, tch, tsf, fm
