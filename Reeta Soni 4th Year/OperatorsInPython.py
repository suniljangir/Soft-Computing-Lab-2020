def Arithmetic(x,y):
    print("Arithmetic Operations")
    print(x+y)
    print(x-y)
    print(x*y)
    print(x/y)    #Division(float)
    print(x//y)   #Division(floor)
    print(x%y)  #modulo 
    print(x**y)  #power
Arithmetic(9,4)

def Relational(x,y):
    print("Relational Operator")
    print(x>y)
    print(x<y)
    print(x==y)
    print(x!=y)
    print(x>=y)
    print(x<=y)
Relational(13,33)    

def Logical(x,y):
    print("Logical Operator")
    print(x and y)
    print(x or y)
    print( not x)   #true if operand is false
Logical(True,False) 

def Bitwise(x,y):
    print("Bitwise Operator")
    print(x & y)
    print(x | y)
    print(~x)   #Returns one’s compliement of the number
    print(x^y)  # XOR:Returns 1 if one of the bit is 1 and other is 0 else returns false
    print(x >> 2)  #bitwise right shift
    print(x << 2)  #bitwise left shift
Bitwise(10,4)    
    
def Assignment(a,b,c):
        print("Assignment Operator")
        c=a+b
        print(c)
        c += a   # c = c + a
        print(c)
        c *= a   # c = c * a
        print(c)
        c /= a   # c = c / a
        print(c)
        c  = 2
        c %= a   #c = c % a
        print(c)
        c **= a   #c = c ** a
        print(c)
        c //= a   #c = c // a
        print(c)
Assignment(21,10,0) 

#SPECIAL OPERATORS
def Identity(a,b):
    print("Identity Operator")
    print(a is b)  #is: True if the operands are identical 
    print (a is not b) #is not: True if the operands are not identical
Identity(3,3)    

def Membership(x):
    print("Membership Operator")
    print('N' in x)
    print("Reeta" not in x)
Membership("ReetaSoni")   
