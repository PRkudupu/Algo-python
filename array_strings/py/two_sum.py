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
# <b>Solution</b>
# <br>2+2=4 <br>
# 4-2=2
#  

# In[3]:


def twosum(ls,k):
    for i in range(len(ls)):
        for j in range(i+1,len(ls)):
            if ls[i]+ls[j] == k:
                return i,j
    return False
num=[2,7,11,15]    
print(twosum(num,9))


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


# In[ ]:





# In[6]:


def twosum(num,target):
    if(len(num)<=1):
        return
    dic ={}
    for i in range(len(num)):
        print("i",i)
        print("num[i]",num[i])
        print("dic",dic)
        if(num[i] in dic):
            return [dic[num[i]],i]
        else:
            dic[target -num[i]] = i
num=[2,3,3]    
twosum(num,6)


# In[25]:


dic ={}
dic[7]=0
dic[8]=1

print(dic[8])


# In[ ]:




