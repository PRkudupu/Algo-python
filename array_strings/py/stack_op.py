#!/usr/bin/env python
# coding: utf-8

# In[5]:


def stack_op():
    stack =[]
    stack.append("open")
    stack.append("close")
    print("stack[0]   ",stack[0])
    print("stack[1]   ",stack[1])
    #Remove the item at the given position in the list, and return it. 
    #If no index is specified, a.pop() removes and returns the last item in the list
    print("stack.pop()   ",stack.pop(0))
    print("stack[0]    ",stack[0])
    print("stack.pop()   ",stack.pop())
stack_op()


# In[ ]:




