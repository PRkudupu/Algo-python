#!/usr/bin/env python
# coding: utf-8

# <b>O (n) </b>

# In[3]:


def max_array(arr):
    max_num=0
    for i in range(len(arr)):
        if arr[i] > max_num:
            max_num=arr[i]
    return max_num
max_array([20,40,60,80,100])


# <b> Using built in function </b>

# In[4]:


def max_array_fn(arr):
    return max(arr)
max_array_fn([20,40,60,80,100])


# <b>O log n</b>

# In[5]:


def mx(ls):
    max_num=0
    m=0
    head=0
    tail=len(ls)-1
    while head <= tail:
        if ls[head] >=ls[tail]:
            m=ls[head]
        elif ls[tail] >=ls[head]:
            m=ls[tail]
        head+=1
        tail-=1
        if m > max_num:
            max_num=m
    return max_num
print(mx([1,500,10,20000]))       


# In[ ]:




