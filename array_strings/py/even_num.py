#!/usr/bin/env python
# coding: utf-8

# Let’s say I give you a list saved in a variable:
# 
# <b>a = [1,2,3,4,10].</b>
# Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.
# 
# output = <b>[2,4,10] </b>

# In[2]:


def even_num(ls):
    return [num for num in ls if num % 2 == 0]
print(even_num([1,2,3,4,10]))

