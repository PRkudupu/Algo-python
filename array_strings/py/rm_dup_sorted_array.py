#!/usr/bin/env python
# coding: utf-8

# Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
# 
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
# 
# <b>Example 1:</b>
# 
# Given nums = [1,1,2],
# 
# Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
# 
# It doesn't matter what you leave beyond the returned length.

# In[1]:


def dup(ls):
    pos=1
    for i in range(1,len(ls)):
        if ls[i]!=ls[i-1]:
            ls[pos]=ls[i]
            pos+=1
    return pos
print(dup([1,2,2,3]))


# In[3]:


remove_dup_sorted([1,3,3,5,6])


# In[2]:


def dup(ls):
    pos=1
    for i in range(1,len(ls)):
        print("i",i)
        if ls[i]!=ls[i-1]:
            ls[pos]=ls[i]
            print("pos",pos)
            print("ls[i]",ls[i])
            print("ls[i-1]",ls[i-1])
            print("ls[pos]",ls[pos])
            pos+=1
    return pos
print(dup([1,2,2,3]))
        


# In[17]:


remove_dup_sorted([1,3,3,5,6])


# In[ ]:




