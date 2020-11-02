#!/usr/bin/env python
# coding: utf-8

# The all() function returns True if all items in an iterable are true, otherwise it returns False.
# 
# If the iterable object is empty, the all() function also returns True.

# In[4]:


def all_use(ls):
    return all(ls)
print(all_use([True,True,True]))


# In[18]:


def all_use(ls):
    stack = []
    for i in ls:
        if i%2 == 0:
            stack.append(True)
            print(all(stack))
        #Here we are appending 3 to the list. This no is not even.
        stack.append(False)
        print(stack)
    return all(stack)
print(all_use([2,4,6]))

