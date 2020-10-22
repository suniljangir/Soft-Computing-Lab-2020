#!/usr/bin/env python
# coding: utf-8
Aim: Demonstrate the use of numpy for matrix operations
# In[1]:


import numpy as np

Creating an array
# In[2]:


#To create an ndarray, we can pass a list, tuple or any array-like object into the array() method, and it will be converted into an ndarray
list1=[0,1,2,3,4]
print("list1 is of tpye:",type(list1))
arr=np.array(list1) 
print("arr is of type:",type(arr))


# In[3]:


np.arange(0,10)


# In[4]:


np.zeros(5)


# In[5]:


np.ones(4)


# In[6]:


np.arange(0,10,3)


# In[7]:


arr1=np.array([1,5,-3,6,1,7,3,0])
print(arr1)
type(arr1)


# Accessing array elements

# In[8]:


a = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(a[1, 1, 2]) #Indexing
print(a[-1,-1,-1]) #Negative indexing
print(a[1,1,:]) #Slicing

Matrix creation
# In[9]:


np.zeros((5,5))


# In[10]:


np.ones((5,7))


# In[11]:


np.ones((4,4))*5


# In[12]:


#2-D Arrays- An array that has 1-D arrays as its elements is called a 2-D array.
x = np.array([[1, 2], [4, 5]])
y = np.array([[7, 8], [9, 10]])
print(x)
print(y)

Matrix operations
# In[13]:


#  add()is used to add matrices
print ("Addition of two matrices: ")
print (np.add(x,y))


# In[14]:


# subtract() is used to subtract matrices
print ("Subtraction of two matrices : ")
print (np.subtract(x,y))


# In[15]:


# divide() is used to divide matrices
print ("Matrix Division : ")
print (np.divide(x,y))


# In[16]:


print ("Element to Element Multiplication of two matrices: ")
print (np.multiply(x,y))


# In[17]:


print ("The product of two matrices : ")
print (np.dot(x,y))


# In[18]:


print ("square root is : ")
print (np.sqrt(x))


# In[19]:


print ("The summation of elements : ")
print (np.sum(y))


# In[20]:


print ("The column wise summation  : ")
print (np.sum(y,axis=0))


# In[21]:


print ("The row wise summation: ")
print (np.sum(y,axis=1))


# In[22]:


# using "T" to transpose the matrix
print ("Matrix transposition : ")
print (x.T)


# In[23]:


#Check Number of Dimensions
#NumPy Arrays provides the ndim attribute that returns an integer that tells us how many dimensions the array have.
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)


# In[24]:


#Higher Dimensional Arrays
#An array can have any number of dimensions.
#When the array is created, you can define the number of dimensions by using the ndmin argument.
arr2 = np.array([1, 2, 3, 4], ndmin=5)
print(arr2)


# In[25]:


np.random.randint(0,100,100)
#randint returns integer value only.


# In[26]:


np.random.randint(0,100,100).reshape(10,10)
# reshape is used to convert array into matrix


# In[27]:


np.random.random(25).reshape(5,5)
#return values between 0 and 1


# In[28]:


np.random.randn(25).reshape(5,5)
# selects value from normal curve


# In[29]:


# to fix randomness,we use seed function of numpy library.
np.random.seed(52)
arr3=np.random.randint(0,100,10)
arr3

Array operations
# In[30]:


arr3.mean()


# In[31]:


arr3.max()


# In[32]:


arr3.min()


# In[33]:


#index of maximum number
arr3.argmax()


# In[34]:


arr3.argmin()


# In[35]:


arr3.argsort()


# In[36]:


arr3.sort()


# In[37]:


arr3


# In[ ]:




