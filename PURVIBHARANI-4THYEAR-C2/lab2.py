#!/usr/bin/env python
# coding: utf-8

# Aim: Write a program to implement various data structures in python and their operations.
1) List
- A list is created by placing all the elements inside square brackets [], separated by comma.
- It can have any number of items and they may be of different types (integer, float, string etc.).
- It can be accessed just like string (e.g. slicing and concatenation) so a list is simple to use and can grow and shrink   automatically as needed.
# In[11]:


list=[1,5.4,0,"a","hi",True,4]
print(list)


# In[12]:


#Accessig list elements
print(list[1]) #Indexing
print(list[-2]) #Negative indexing means beginning from the end, -1 refers to the last item, -2 refers to the second last item etc.
print(list[::2]) #slicing [start:end:step_size]
print(list[1:5])
#The search will start at index 1 (included) and end at index 5 (excluded).


# In[13]:


#Change Item Value
list[0]=10
print(list) #element at index 0 is now changed to 10.


# In[14]:


#Add Items
# To add an item to the end of the list, use the append() method
list.append(45)
#To add an item at the specified index, use the insert() method
list.insert(3,"blue")
print(list)


# In[15]:


#To remove an item from the list "pop " keyword is used
#The remove() method removes the specified item
list.remove("hello")
#The pop() method removes the specified index,or the last item if index is not specified
list.pop()
#The del keyword removes the specified index
del list[1]
print(list)


# In[16]:


list.reverse() #To reverse the list
print(list)
print(len(list)) #To calculate length of the list


# In[17]:


#Looping through a list
for item in list:
    print(item)


# In[18]:


#sort the list
list1=[3,9,4,1,0,7,-3]
list1.sort()
print(list1)


# In[19]:


#Joining 2 lists
list2=list+list1
print(list2)
#list.extend(list1) also serves the same purpose.


# In[20]:


#The clear() method empties the list
list1.clear()
print(list1)

2) Dictionary
Dictionary in Python is similar to hash or maps in other languages.
It consists of key-value pairs.
The value can be accessed by unique key in the dictionary.
Keys are unique & immutable objects.
Syntax: dictionary = {"key name": value}
# In[21]:


d={"one":1,"two":2,"three":3}
print(d)


# In[22]:


#for acessing items
print(d["two"])
#We can also use "get" keyword
print(d.get("two"))


# In[23]:


# To change the values 
d["one"]=10
print(d)


# In[24]:


#Looping through dictionary

for x in d:
    print(x)
    
#For Printing all the values one by one

for x in d:
    print(d[x])


# In[25]:


#We can use "values" keyword to return the value of dict.
for x in d.values():
    print(x)


# In[26]:


#Loop through both keys and values, by using the items() method:
for x, y in d.items():
    print(x,y)


# In[27]:


#For checking the length of dictonary
print(len(d))


# In[28]:


#To add items in dictionary
d["four"]=4
print(d)


# In[29]:


#To remove items from dictionary
d.pop("one")
print(d)


# In[30]:


#The del keyword removes the item with the specified key name
del d["three"]
print(d)


# In[31]:


d.clear()
print(d)

3) Tuple
-Tuples work exactly like lists except they are immutable, i.e. they can’t be changed in place.
-They are normally written inside parentheses to distinguish them from lists (which use square brackets), parentheses aren’t always necessary.
-Since tuples are immutable, their length is fixed. To grow or shrink a tuple, a new tuple must be created.
# In[32]:


tup = (1, "a", "string", 1+2) 
print (tup) 
#Accessing tuple items
print (tup[1]) 
print(tup[1:3])
print(tup[::-1])#print in reverse order


# In[33]:


#Code for concatenating two tuples
tuple1=(0,1,2,3)
tuple2=("a","b","c")
print(tuple1+tuple2)


# In[34]:


#nesting tuples
tuple3=(tuple1,tuple2)
print(tuple3)


# In[35]:


#Use of multiplication operator
tup=("a",)*5
print(tup)


# In[37]:


#Tuples are immutable
tuple1[0]=4
print(tuple1)
#Once a tuple is created, you cannot add items to it. Tuples are unchangeable.


# In[38]:


#Finding the length of tuple
print(len(tup))


# In[39]:


#Code for converting a list and a string into a tuple
list1 = [0, 1, 2] 
print(tuple(list1)) 
print(tuple('hello')) # string


# In[40]:


#Tuples are unchangeable, so you cannot remove items from it, but you can delete the tuple completely
del(tup)

4) Set
-A set is a collection which is unordered and unindexed.
-In Python, sets are written with curly brackets.
# In[41]:


set1 = {"a", "b", "c"}
print(set1)


# In[42]:


#Accessing Items
#You cannot access items in a set by referring to an index or a key but you can loop through the set items using a "for" loop, 
for x in set1:
  print(x)


# In[43]:


#To check for the item
print("b" in set1)
print("f" in set1)


# In[44]:


#Once a set is created, you cannot change its items but new items can be added.
#Add Items
set1.add("h")
print(set1)

#Add multiple items to a set, using the update() method:
set1.update(["x", "y", "z"])
print(set1)


# In[45]:


#To check the length
print(len(set1))


# In[46]:


#To remove an item in a set, use the remove(), or the discard() method.
set1.remove("h")
print(set1)
#Sets are unordered, so when using the pop() method, you will not know which item that gets removed.
set1.pop()
print(set1)


# In[47]:


#The clear() method empties the set:
set1.clear()
print(set1)


# In[48]:


#Joining 2 sets
#The union() method returns a new set with all items from both sets:
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)
#The update() method inserts the items in set2 into set1
set1.update(set2)
print(set1)

