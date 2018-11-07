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

# In[9]:


def max_array_div(arr):
    max_num,max_so_far,head,tail =arr[0],0,0,len(arr)-1
    while head <=tail:
        if arr[head] > arr[tail]:
            max_so_far =arr[head]
        else:
            max_so_far =arr[tail]
        if max_so_far > max_num:
            max_num=max_so_far
        head+=1
        tail-=1
    return max_num
max_array_div([20,40,60,80,100])        


# In[ ]:




