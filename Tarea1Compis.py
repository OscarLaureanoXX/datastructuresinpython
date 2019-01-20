"""


Tarea 1

Desarrolla y/o documenta una implementación apropiada para las siguientes clases: STACK (lifo), 
QUEUE (fifo), TABLE/HASH/DICTIONARY (order),.. (* las puedes implementar “desde 0” o usar alguna 
librería “pública” *) Las clases deben contener métodos para soportar las principales operaciones 
de acceso y manipulación (clásicas). 
"""

# ---------------------------------------------------------------------
# ---------------------------- Stack ----------------------------------
# ---------------------------------------------------------------------

# Implemented with a list, where the first element
# is considered to be the Top of the stack
"""                     Top

                        10
  [10, 12, 9, 1]   =>   12
                        9
                        1

                        Bottom      
"""
# Methods:
#   __init__ : Creates an empty stack
#   push : Pushes the element at the beginning of the list (Top of the stack)
#   pop : Returns and pops the element at the Top of the stack (None if the stack is empty)
#   peek: Returns the element at the Top of the stack (None if the stack is empty)
#   isEmpty: Returns true when stack is empty, false otherwise
#   print: Displays all the elements of the stack


class Stack:
    def __init__(self): # Init as an empty stack
        self.list = []

    def push(self, element): # Pushing the element at the beginning of the list (Top)
        self.list.insert(0, element)

    def pop(self): # Returns and pops the element at the Top of the stack
        if self.isEmpty():
            return None
        else:
            return self.list.pop(0)

    def peek(self): # Returns the element at the Top of the stack 
        if self.isEmpty():
            return None
        else:
            return self.list[0]

    def isEmpty(self): # Returns true when stack is empty, false otherwise
        return self.list == []
    
    def print(self): # Displays all the elements of the stack
        if self.isEmpty():
            print ("Stack Empty")
        else:
            for elem in self.list:
                print(elem)
    
# Implementation of the stack: 

# Creating the stack
s = Stack()

# Pushing three numbers in
s.push(20)
s.push(6)
s.push(10)

# Displaying the stack
s.print()

# Showing the peek only
print(s.peek())

# Popping the top element
print(s.pop())

# Asking if the stack is empty
print(s.isEmpty())

# Popping two more elements
print(s.pop())
print(s.pop())

# Asking if the stack is empty
print(s.isEmpty())


# ---------------------------------------------------------------------
# ---------------------------- QUEUE ----------------------------------
# ---------------------------------------------------------------------

# Implemented with a list where the first element is the front 
# and the last is the back
""" 
   Front [1, 40, 23, 19, 12] Back 
"""

# Methods:
#   __init__ : Creates an empty stack
#   insert : Inserts the element at the back of the queue
#   remove : Removes and returns the element at the front of the queue (None if the queue is empty)
#   front: Returns the element at the front of the queue (None if the queue is empty)
#   isEmpty: Returns true when the queue is empty, false otherwise
#   print: Displays all the elements of the queue

class Queue:
    def __init__(self):
        self.list = []
    
    def insert(self, element):
        self.list.append(element)

    def remove(self):
        if self.isEmpty():
            return None
        else:
            return self.list.pop(0)
    
    def front(self):
        if self.isEmpty():
            return None
        else:
            return self.list[0]

    def isEmpty(self): 
        return self.list == []
    
    def print(self):
        if self.isEmpty():
            print("Empty Queue")
        else:
            print(self.list)

# Implementation of the queue:

# Creating an empty queue
q = Queue()

# Inserting three elements
q.insert(10)
q.insert(20)
q.insert(35)

# Displaying the front
print(q.front())

# Displaying all the elements
q.print()

# Asking if the queue is empty
print(q.isEmpty())

# Removing one element
print(q.remove())

# Displaying all the elements
q.print()

# Removing the rest of the elements
print(q.remove())
print(q.remove())

# Asking if the queue is empty
print(q.isEmpty())


# ---------------------------------------------------------------------
# -------------------- TABLE/HASH/DICTIONARY  -------------------------
# ---------------------------------------------------------------------

# Using the existing dictionary in python

# Creating a dictionary:
phones = {'elda' : 911, 'wicho' : 92102, 'roque' : 133212}

# Inserting new elements:
phones['yolanda'] = 738923

# Deleting elements:
del phones['roque']

# Checkig if it exists:
'roque' in phones
'elda' in phones

# Getting one number by its key:
phones['elda']

# Provides the list of all the keys sorted:
sorted(phones)

# Provides the list of all the keys in insertion order:
list(phones)