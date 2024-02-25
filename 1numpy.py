# -*- coding: utf-8 -*-
"""numpy1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1L-0OrmugcMRmQDKrShy5FsfZ2cSYiMfH
"""

import numpy as np

py_list=[1,2,3,4,5,6,7,8,9]

#numpy array
np_array=np.array([1,2,3,4,5,6,7,8,9])

print(type(py_list))
print(type(np_array))

py_multi=[[1,2,3],[4,5,6],[7,8,9]]
np_multi=np_array.reshape(3,3)

print(py_multi)
print(np_multi)

print(np_array.ndim)
print(np_multi.ndim)

print(np_array.shape)
print(np_multi.shape)