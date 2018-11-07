#!/usr/bin/env python
# coding: utf-8

# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# 
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# 
# #### Example:
# 
# Given nums = [2, 7, 11, 15], target = 9,
# 
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
#  

# In[14]:


def twosum(num,target):
    if(len(num)<=1):
        return
    dic ={}
    for i in range(len(num)):
        if(num[i] in dic):
            return [dic[num[i]],i]
        else:
            dic[target -num[i]] = i
num=[2,7,11,15]    
twosum(num,9)


# In[33]:


def twosum(num,target):
    if(len(num)<=1):
        return
    dic ={}
    for i in range(len(num)):
        print("i",i)
        print("num[i]",num[i])
        if(num[i] in dic):
            print("inside if")
            print([dic[num[i]],i])
            return [dic[num[i]],i]
        else:
            print("inside else")
            print("sub {}".format(target-num[i]))
            dic[target -num[i]] = i
num=[2,7,11,15]    
twosum(num,9)


# In[25]:


dic ={}
dic[7]=0
dic[8]=1

print(dic[8])


# In[ ]:




