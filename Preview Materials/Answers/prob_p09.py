# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 15:22:44 2020

@author: TanXiao
"""

a=input()
b=input()
c=input()
# Alice and Bob swapped their paper.
temp=a
a=b
b=temp
# Alice and Charlotte swapped their paper.
temp=a
a=c
c=temp
# Bob and Alice swapped their paper.
temp=b
b=a
a=temp
# Bob and Charlotte swapped their paper.
temp=b
b=c
c=temp
# Alice erased the sentence on her paper.Alice copied the sentence on Charlotte’s paper to her paper.
a=c
# Alice and Bob swapped their paper.
t=a
a=b
b=t
# Charlotte and Bob swapped their paper.
t=b
b=c
c=t
# Charlotte and Alice swapped their paper.
t=c
c=a
a=t

print(a)
print(b)
print(c)