# -*- coding: utf-8 -*-
"""3numpyArray_index.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1O1hWM0MhGE6h9kSi1te4G4kunfFhp9P8
"""

import numpy as np

numbers=np.array([0,5,10,15,20,25,50,7,85])

'''
result=numbers[5]
result=numbers[-1]
result=numbers[0:3]
result=numbers[:3]
result=numbers[3:]
result=numbers[::]  #all list
result=numbers[::-1]
'''

'''
numbers2=np.array([[0,5,10],[15,20,25],[50,75,85]])
result=numbers2[0]
result=numbers2[2]
result=numbers2[0,2]
result=numbers2[2,1]
result=numbers2[:,2]
result=numbers2[:,0]
result=numbers2[:,0:2]
result=numbers2[-1,:]
result=numbers2[:2,:2]
print(result)
'''

arr1=np.arange(0,10)
#arr2=arr1 #reference
arr2=arr1.copy()

arr2[0]=20
print(arr1)
print(arr2)