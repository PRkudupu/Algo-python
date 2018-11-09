#!/usr/bin/env python
# coding: utf-8

# ### Given 2 list return unique elements from both the list
# <b>Input</b>
# s1=[1,2,3]
# 
# s2=[3,4,5]
# 
# <b>output </b>
# [1,2,4,5]

# In[5]:


def unique_list(s1,s2):
    new_list = []
    for i in s1:
        if i not in s2:
            new_list.append(i)
    for j in s2:
        if j not in s1:
            new_list.append(j)
    return new_list

print(no_repeat_list([1,2,3],[3,4,5]))
            


# In[ ]:




