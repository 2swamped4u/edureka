#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 06:20:17 2021

@author: Santa
"""

import array as arr
a = arr.array('d', [1.1, 2.1, 3.1])
a.append(3.4)
print("Array a = ", a)
b = arr.array('d', [2.1, 3.2, 4.6])
b.extend([4.5, 3.6, 7.2])
print("Array b = ", b)
c = arr.array('d', [1.1, 2.1, 3.1])
c.insert(2, 3.4)
print("Arrays c = ", c)
