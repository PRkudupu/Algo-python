#!/usr/bin/env python
# coding: utf-8

# ### Remove Duplicates from Sorted Array
# Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
# 
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with <b>O(1)</b> extra memory.
# 
# Example 1:
# 
# <b>Given nums = [1,1,2],</b>
# 
# Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
# 
# It doesn't matter what you leave beyond the returned length.
# Example 2:
# 
# <b>Given nums = [0,0,1,1,1,2,2,3,3,4],</b>
# 
# Your function should return length = 5, with the first five elements of nums being modified to <b>0, 1, 2, 3, and 4 </b>respectively.
# 
# It doesn't matter what values are set beyond the returned length.
# Clarification:
# 
# Confused why the returned value is an integer but your answer is an array?
# 
# Note that the input array is passed in by reference, which means modification to the input array will be known to the caller as well.
# 
# Internally you can think of this:
# 
# ![alt text](image/remdups.JPG)

# In[6]:


def removeDuplicates(ls):
    if not ls:
        return 0

    newTail = 0

    for i in range(1, len(ls)):
        if ls[i] != ls[newTail]:
            newTail += 1
            ls[newTail] = ls[i]

    return newTail + 1

print(removeDuplicates([1,1,2,2]))


# In[ ]:




