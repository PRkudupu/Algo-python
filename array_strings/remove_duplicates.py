#!/usr/bin/env python
# coding: utf-8

# Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
# 
# <b>Example 1:</b>
# Given nums = [1,1,2],
# Your function should return new array without duplicates
# 
# <b>return =[1,2]</b>

# In[80]:


def remove_dup(dup_list):
    new_list =[]
    for i in dup_list:
        if i not in new_list:
            new_list.append(i)
    return new_list   


# In[7]:


def remove_dup(dup_list):
    return (list(set(dup_list)))


# In[8]:


remove_dup([1,2,2,4,4])


# In[ ]:




