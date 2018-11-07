#!/usr/bin/env python
# coding: utf-8

# ### Print parts of the array

# In[5]:


def print_part(ls):
    print("0 to 3",ls[0:3])
    print("Increement by 2",ls[0:3:2])
    print("Increement by 3",ls[0:3:3])
    print("print till the end",ls[0:-1])
    print("Reverse the list",ls[::-1])
    print("slice",slice(ls[0:2]))
print_part([1,4,5,8,10,12,15])

