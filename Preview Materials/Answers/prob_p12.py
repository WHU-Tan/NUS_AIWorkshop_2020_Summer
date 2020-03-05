# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 17:18:49 2020

@author: TanXiao
"""

a=int(input())
b=int(input())
c=int(input())

delta=b**2-4*a*c
x1=(-b-delta**0.5)/(2*a)
x2=(-b+delta**0.5)/(2*a)

#output
print(x1)
print(x2)