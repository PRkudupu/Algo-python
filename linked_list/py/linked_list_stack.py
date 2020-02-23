#!/usr/bin/env python
# coding: utf-8

# # Implement a stack using a linked list
# ## 1. Define a `Node` class
# Since we'll be implementing a linked list for this, we know that we'll need a `Node` class like we used earlier in this lesson.
# 

# In[1]:


#Node class
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None


# ## 2. Create the `Stack` class and its `__init__` method
# 
# In the cell below, see if you can write the `__init__` method for our `Stack` class. It will need two attributes:
# * A `head` attribute to keep track of the first node in the linked list
# * A `num_elements` attribute to keep track of how many items are in the stack

# In[4]:


class Stack:
    def __init__(self):
        self.head = None # No items in the stack, so head should be None
        self.num_elements = 0 # No items in the stack, so num_elements should be 0


# ## 3. Add the `push` method
# 
# Next, we need to define our `push` method, so that we have a way of adding elements to the top of the stack. First, have a look at the walkthrough:

# In[5]:


def push(self, value):
        new_node = Node(value)        
        # if stack is empty
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head    # place the new node at the head of the linked list (top)
            self.head = new_node

   


# Now give it a try for yourself. In the cell below, add the `push` method:
# * The method will need to have a parameter for the `value` that you want to push
# * You'll then need to create a new `Node` object with this value and link it to the list
# * Remember that we want to add new items at the head of the stack, not the tail!
# * Once you've added the new node, you'll want to increment `num_elements`

# In[6]:


class Stack:
    
    def __init__(self):
        self.head = None
        self.num_elements = 0
        
    def push(self, value):
        new_node = Node(value)        
        # if stack is empty
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head    # place the new node at the head of the linked list (top)
            self.head = new_node

        self.num_elements += 1


# ## 4. Add the `size` and `is_empty` methods
# 
# When we implemented a stack using an array, we had these same methods. They'll work exactly the same way here—they aren't affected by the use of a linked list versus an array.
# * Add a `size` method that returns the current size of the stack
# * Add an `is_empty` method that returns `True` if the stack is empty and `False` otherwise

# In[7]:


class Stack:
    
    def __init__(self):
        self.head = None
        self.num_elements = 0
        
    def push(self, value):
        new_node = Node(value)
        # if stack is empty
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head # place the new node at the head (top) of the linked list
            self.head = new_node

        self.num_elements += 1
    #size method   
    def size(self):
        return self.num_elements
    #is empty method
    def is_empty(self):
        return self.num_elements == 0


# ## 5. Add the `pop` method
# 
# The last thing we need to do is add the `pop` method. First, here's a walkthrough that describes how the method works:

# Now try it yourself. The method needs to:
# * Check if the stack is empty and, if it is, return `None`
# * Get the value from the `head` node and put it in a local variable
# * Move the `head` so that it refers to the next item in the list
# * Return the value we got earlier

# In[8]:


class Stack:
    
    def __init__(self):
        self.head = None
        self.num_elements = 0
        
    def push(self, value):
        new_node = Node(value)
        # if stack is empty
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head # place the new node at the head (top) of the linked list
            self.head = new_node

        self.num_elements += 1
        
    def pop(self):
        if self.is_empty():
            return
        
        value = self.head.value # copy data to a local variable
        self.head = self.head.next # move head pointer to point to next node (top is removed by doing so)
        self.num_elements -= 1
        return value
    
    def size(self):
        return self.num_elements
    
    def is_empty(self):
        return self.num_elements == 0


# ## Test it!
# Now that we've completed our `Stack` class, let's test it to make sure it all works as expected.

# In[9]:


# Setup
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)

# Test size
print ("Pass" if (stack.size() == 5) else "Fail")

# Test pop
print ("Pass" if (stack.pop() == 50) else "Fail")

# Test push
stack.push(60)
print ("Pass" if (stack.pop() == 60) else "Fail")
print ("Pass" if (stack.pop() == 40) else "Fail")
print ("Pass" if (stack.pop() == 30) else "Fail")
stack.push(50)
print ("Pass" if (stack.size() == 3) else "Fail")


# ## Time complexity of stacks using linked lists
# 
# Notice that if we pop or push an element with this stack, there's no traversal. We simply add or remove the item from the head of the linked list, and update the `head` reference. So with our linked list implementaion, `pop` and `push` have a time complexity of O(1).
# 
# Also notice that using a linked list avoids the issue we ran into when we implemented our stack using an array. In that case, adding an item to the stack was fine—until we ran out of space. Then we would have to create an entirely new (larger) array and copy over all of the references from the old array.
# 
# That happened because, with an array, we had to specify some initial size (in other words, we had to set aside a contiguous block of memory in advance). But with a linked list, the nodes do not need to be contiguous. They can be scattered in different locations of memory, an that works just fine. This means that with a linked list, we can simply append as many nodes as we like. Using that as the underlying data structure for our stack means that we never run out of capacity, so pushing and popping items will always have a time complexity of O(1).
# 
# 
