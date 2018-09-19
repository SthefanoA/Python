#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 16:09:23 2017

@author: Brandon_Garry, Garry, Brandon
"""

#lab02.py

import numpy as np

fm = "{:8.4f}"

#FINISHED
#p01
p01 = ((14.8**2 + 6.5**2)/(3.8**2)) + ((55) / (np.sqrt(2) + 14))
print(" p01." + fm.format(p01))

#p02
p02 = (-3.5**3) + ((np.exp(6))/(np.log(524))) + 206**(1/3)
print(" p02." + fm.format(p02))

#p03
p03 = (16.5**2)*(8.4 - (np.sqrt(70)))/(4.3**2 - 17.3)
print(" p03." + fm.format(p03))

#p04
p04 = (5.2**3 - 6.4**2 + 3)/(1.6**8 - 2) + ((13.3/5)**1.5)
print(" p04." + fm.format(p04))

#p05
p05 = (15)*((np.sqrt(10)) + 3.7**2)/((np.log10(1365)) + 1.9)
print(" p05." + fm.format(p05))

#06
p06 = ((2.5**3)*(16 - (216/22))/(1.7**4 + 14) + 2050**(1/4))
print(" p06." + fm.format(p06))

#p07
p07 = (2.3**2 * 1.7)/(np.sqrt((1-(.8**2))**2 + (2 - (np.sqrt(.87)))**2))
print(" p07." + fm.format(p07))

#p08
p08 = 2.34 + (.5)*(2.7)*(5.9**2 - 2.4**2) + (9.8)*(np.log(51))
print(" p08." + fm.format(p08))

#p09
p09 = (np.sin(7*np.pi/9))/((np.cos(5*np.pi/7))**2)+ (1/7)*(np.tan(5*np.pi/12))
print(" p09." + fm.format(p09))

#p10
p10 = (np.tan(np.deg2rad(64)))/((np.cos(np.deg2rad(14)))**2) - (3)*(np.sin(np.deg2rad(80)))/(.9**(1/3)) + (np.cos(np.deg2rad(55)))/(np.sin(np.deg2rad(11)))
print(" p10." + fm.format(p10))

#p11
x = 2.34
p11a = (2)*(x)**4  - (6)*(x)**3 + (14.8)*(x)**2 + 9.1
print("p11a." + fm.format(p11a))

p11b = (np.exp((2)*(x)))/(np.sqrt(14 + (x)**2 - (x)))
print("p11b." + fm.format(p11b))

 #p12
t = 6.8
p12a = np.log(np.absolute(t**2 - t**3))
print("p12a." + fm.format(p12a))
 
p12b = (75/(2*t)) * (np.cos((.8)*(t) - 3))
print("p12b." + fm.format(p12b))

#p13
x = 8.3
y = 2.4
p13a = x**2 + y**2 - (x**2/y**2)
print("p13a." + fm.format(p13a))

p13b = np.sqrt(x*y) - np.sqrt(x+y) + ((x-y)/(x-2*y))**2 - np.sqrt(x/y)
print("p13b." + fm.format(p13b))

#p14
a = 13
b = 4.2
c = 4*b/a
d = (a*b*c)/(a+b+c)
p14a = (a*b)/(c + d) + (d*a)/(c*b) - (a-(b**2))*(c+d)
print("p14a." + fm.format(p14a))

p14b = (np.sqrt((a**2)+(b**2)))/(d-c) + (np.log(np.absolute(b-a+c-d)))
print("p14a." +fm.format(p14b))

#p15
p15a = np.log(.085)/np.log(4)
print("p15a." + fm.format(p15a))

p15b = np.log(1500)/np.log(6)
print("p15b." + fm.format(p15b))