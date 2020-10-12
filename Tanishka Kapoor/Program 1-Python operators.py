print("Aim: To implement various operators in python.")

#ARITHMETIC OPERATORS

a = 21
b = 10
c = 0

c = a + b
print("Line 1 - Value of c is ", c)

c = a - b
print("Line 2 - Value of c is ", c) 

c = a * b
print("Line 3 - Value of c is ", c) 

c = a / b
print("Line 4 - Value of c is ", c)

c = a % b
print("Line 5 - Value of c is ", c)

a = 2
b = 3
c = a**b 
print("Line 6 - Value of c is ", c)

a = 10
b = 5
c = a//b 
print("Line 7 - Value of c is ", c)


#COMPARISON OPERATORS
x = 10
y = 12

# Output: x > y is False
print('x > y is',x>y)

# Output: x < y is True
print('x < y is',x<y)

# Output: x == y is False
print('x == y is',x==y)

# Output: x != y is True
print('x != y is',x!=y)

# Output: x >= y is False
print('x >= y is',x>=y)

# Output: x <= y is True
print('x <= y is',x<=y)


#LOGICAL OPERATORS
x = True
y = False

print('x and y is',x and y)

print('x or y is',x or y)

print('not x is',not x)

#IDENTITY OPERATORS
x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1,2,3]
y3 = [1,2,3]

# Output: False
print(x1 is not y1)

# Output: True
print(x2 is y2)

# Output: False
print(x3 is y3)


#MEMBERSHIP OPERATORS
x = 'Hello world'
y = {1:'a',2:'b'}

# Output: True
print('H' in x)

# Output: True
print('hello' not in x)

# Output: True
print(1 in y)

# Output: False
print('a' in y)



"""
OUTPUT OF THE PROGRAM
Line 1 - Value of c is  31
Line 2 - Value of c is  11
Line 3 - Value of c is  210
Line 4 - Value of c is  2.1
Line 5 - Value of c is  1
Line 6 - Value of c is  8
Line 7 - Value of c is  2
x > y is False
x < y is True
x == y is False
x != y is True
x >= y is False
x <= y is True
x and y is False
x or y is True
not x is False
False
True
False
True
True
True
False
"""



