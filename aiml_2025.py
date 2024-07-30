# -*- coding: utf-8 -*-
"""AIML/2025.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ZvFbFYaOYObu9vdvxakp2UFHeOsE-tIk
"""

import numpy as np
import pandas as pd

# Lists
list1 = [1, 2, 3, 4, 5]
print(list1)
print(type(list1))

# Arrays
array1 = np.array([6, 7, 8, 9, 10])
print(array1)
print(type(array1))

# Mathematical operations:-

# Multiplication
result_list = [x * 2 for x in list1]
result_array = array1 * 2
print(result_list)
print(result_array)

# Division
result1 = [x / 2 for x in list1]
result2 = array1 / 2
print(result1)
print(result2)