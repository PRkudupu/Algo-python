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

# In[2]:


def remove_dup_sorted(A):
    if not A:
        return 0
    newTail=0
    for i in range(1,len(A)):
         if A[i] != A[newTail]:
            newTail +=1
            A[newTail]=A[i]
    return newTail +1


# In[3]:


remove_dup_sorted([1,3,3,5,6])


# In[16]:


def remove_dup_sorted(A):
    if not A:
        return 0
    newTail=0
    for i in range(1,len(A)):
        print("start A[i] : {}".format(A[i]))
        print("A[newTail] : {}".format(A[newTail]))
        print("newTail :{} ".format(newTail))
        print("i :{}".format(i))
        print("end A[i] != A[newTail] {}".format(A[i] != A[newTail]))
        if A[i] != A[newTail]:
            newTail +=1
            A[newTail]=A[i]
    return newTail +1


# In[17]:


remove_dup_sorted([1,3,3,5,6])


# In[ ]:




