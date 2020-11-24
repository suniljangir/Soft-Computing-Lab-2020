#LISTS

listt = [] #create empty list
print(listt)
listt = [1, 2, 3, 'example', 3.132] #creating list with data
print(listt)
"""
Output:
[]
[1, 2, 3, ‘example’, 3.132]
"""


#ADDING ELEMENTS
llist = [1, 2, 3]
print(llist)
llist.append([555, 12]) #add as a single element
print(llist)
llist.extend([234, 'more_example']) #add as different elements
print(llist)
llist.insert(1, 'insert_example') #add element i
print(llist)

#DELETING ELEMENTS
listt = [1, 2, 3, 'example', 3.132, 10, 30]
del listt[5] #delete element at index 5
print(listt)
listt.remove('example') #remove element with value
print(listt)
a = listt.pop(1) #pop element from list
print('Popped Element: ', a, ' List remaining: ', listt)
listt.clear() #empty the list
print(my_list)

#ACCESSING ELEMENTS
my_list = [1, 2, 3, 'example', 3.132, 10, 30]
for element in my_list: #access elements one by one
    print(element)
print(my_list) #access all elements
print(my_list[3]) #access index 3 element
print(my_list[0:2]) #access elements from 0 to 1 and exclude 2
print(my_list[::-1]) #access elements in reverse

#------------------------------------------------------------------------------

#DICTIONARY

my_dict = {} #empty dictionary
print(my_dict)
my_dict = {1: 'Python', 2: 'Java'} #dictionary with elements
print(my_dict)
"""
Output:
{}
{1: ‘Python’, 2: ‘Java’}
"""

#UPDATING AND ADDING
my_dict = {'First': 'Python', 'Second': 'Java'}
print(my_dict)
my_dict['Second'] = 'C++' #changing element
print(my_dict)
my_dict['Third'] = 'Ruby' #adding key-value pair
print(my_dict)

#DELETING
my_dict = {'First': 'Python', 'Second': 'Java', 'Third': 'Ruby'}
a = my_dict.pop('Third') #pop element
print('Value:', a)
print('Dictionary:', my_dict)
b = my_dict.popitem() #pop the key-value pair
print('Key, value pair:', b)
print('Dictionary', my_dict)
my_dict.clear() #empty dictionary
print('n', my_dict)

#ACCESSING
my_dict = {'First': 'Python', 'Second': 'Java'}
print(my_dict['First']) #access elements using keys
print(my_dict.get('Second'))

#APPENDING
my_tuple = (1, 2, 3)
my_tuple = my_tuple + (4, 5, 6) #add elements
print(my_tuple)

#-------------------------------------------------------------------------------

#SETS
my_set = {1, 2, 3, 4, 5, 5, 5} #create set
print(my_set)

"""Output:
{1, 2, 3, 4, 5}"""

#ADDING
my_set = {1, 2, 3}
my_set.add(4) #add element to set
print(my_set)

#OPERATIONS
my_set = {1, 2, 3, 4}
my_set_2 = {3, 4, 5, 6}
print(my_set.union(my_set_2), '----------', my_set | my_set_2)
print(my_set.intersection(my_set_2), '----------', my_set & my_set_2)
print(my_set.difference(my_set_2), '----------', my_set - my_set_2)
print(my_set.symmetric_difference(my_set_2), '----------', my_set ^ my_set_2)
my_set.clear()
print(my_set)

#-------------------------------------------------------------------------------
#TUPLE
my_tuple = (1, 2, 3) #create tuple
print(my_tuple) 
"""
Output:
(1, 2, 3)
"""

#ACCESSING
my_tuple2 = (1, 2, 3, 'edureka') #access elements
for x in my_tuple2:
    print(x)
print(my_tuple2)
print(my_tuple2[0])
print(my_tuple2[:])
print(my_tuple2[3][4])

#APPENDING
my_tuple = (1, 2, 3)
my_tuple = my_tuple + (4, 5, 6) #add elements
print(my_tuple)

#-----------------------------------------------------------------------------
"""
User-Defined Data Structures
Arrays vs. Lists
Arrays and lists are the same structure with one difference. Lists allow heterogeneous data element storage whereas
Arrays allow only homogenous elements to bestored within them.
Stacks are linear Data Structures which are based on the principle of Last-In-First-Out (LIFO) where data which is entered last will be the first to get accessed. It is
built using the array structure and has operations namely, pushing (adding) elements, popping (deleting) elements and accessing elements only from one point in the
stack called as the TOP.
Queue
A queue is also a linear data structure which is based on the principle of First-In-First-Out (FIFO) where the data entered first
will be accessed first. It is built using the array structure and has operations which can be performed from both ends of the Queue, that is, head-tail or front-back
Tree
Trees are non-linear Data Structures which have root and nodes. The root is the node from where the data originates and the nodes are the other data points that are
available to us. The node that precedes is the parent and the node after is called the child.
Linked List
Linked lists are linear Data Structures which are not stored consequently but are linked with each other using pointers. The node of a linked list is composed
of data and a pointer called next.
Graph
Graphs are used to store data collection of points called vertices (nodes) and edges (edges). Graphs can be called as the most accurate representation of a real-world map.
Graph
Graphs are used to store data collection of points called vertices (nodes) and edges (edges). Graphs can be called as the most accurate representation of a real-world map.
"""
