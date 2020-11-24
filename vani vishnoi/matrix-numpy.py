"""
A matrix is a two-dimensional data structure where numbers are arranged
into rows and columns.
Python doesn't have a built-in type for matrices. However,
we can treat list of a list as a matrix. For example:
A = [[1, 4, 5], 
    [-5, 8, 9]]
NumPy is a package for scientific computing which has support for a powerful
N-dimensional array object.
NumPy provides multidimensional array of numbers (which is actually an object). Let's take an example:
import numpy as np
a = np.array([1, 2, 3])
print(a)               # Output: [1, 2, 3]
print(type(a))         # Output: <class 'numpy.ndarray'>
"""

#CREATING A NUMPY ARRAY
import numpy as np

A = np.array([[1, 2, 3], [3, 4, 5]])
print(A)

A = np.array([[1.1, 2, 3], [3, 4, 5]]) # Array of floats
print(A)

A = np.array([[1, 2, 3], [3, 4, 5]], dtype = complex) # Array of complex numbers
print(A)

#Array of zeros and ones

import numpy as np

zeors_array = np.zeros( (2, 3) )
print(zeors_array)

'''
 Output:
 [[0. 0. 0.]
  [0. 0. 0.]]
'''

ones_array = np.ones( (1, 5), dtype=np.int32 ) # specifying dtype
print(ones_array)      # Output: [[1 1 1 1 1]]

#Using arange() and shape()

import numpy as np

A = np.arange(4)
print('A =', A)

B = np.arange(12).reshape(2, 6)
print('B =', B)

#MATRIX OPERATIONS
#ADDITION

import numpy as np

A = np.array([[2, 4], [5, -6]])
B = np.array([[9, -3], [3, 6]])
C = A + B      # element wise addition
print(C)

#MULTIPLICATION
import numpy as np

A = np.array([[3, 6, 7], [5, -3, 0]])
B = np.array([[1, 1], [2, 1], [3, -3]])
C = A.dot(B)
print(C)

#TRANSPOSE

import numpy as np

A = np.array([[1, 1], [2, 1], [3, -3]])
print(A.transpose())

#ACCESSING ELEMENTS

import numpy as np
A = np.array([2, 4, 6, 8, 10])

print("A[0] =", A[0])     # First element     
print("A[2] =", A[2])     # Third element 
print("A[-1] =", A[-1])   # Last element

#SLICING
import numpy as np
letters = np.array([1, 3, 5, 7, 9, 7, 5])

# 3rd to 5th elements
print(letters[2:5])        # Output: [5, 7, 9]

#--------------------------------------------------------------------------
#ARITHMETIC OPERATIONS ON MATRIX
import numpy 
  
# initializing matrices 
x = numpy.array([[1, 2], [4, 5]]) 
y = numpy.array([[7, 8], [9, 10]]) 
  
# using add() to add matrices 
print ("The element wise addition of matrix is : ") 
print (numpy.add(x,y)) 
  
# using subtract() to subtract matrices 
print ("The element wise subtraction of matrix is : ") 
print (numpy.subtract(x,y)) 
  
# using divide() to divide matrices 
print ("The element wise division of matrix is : ") 
print (numpy.divide(x,y))

print ("The element wise multiplication of matrix is : ") 
print (numpy.multiply(x,y)) 
  
# using dot() to multiply matrices 
print ("The product of matrices is : ") 
print (numpy.dot(x,y))

# using sqrt() to print the square root of matrix 
print ("The element wise square root is : ") 
print (numpy.sqrt(x)) 
  
# using sum() to print summation of all elements of matrix 
print ("The summation of all matrix element is : ") 
print (numpy.sum(y)) 
  
# using sum(axis=0) to print summation of all columns of matrix 
print ("The column wise summation of all matrix  is : ") 
print (numpy.sum(y,axis=0)) 
