#!/usr/bin/env python
# coding: utf-8

# In given array find the duplicate odd number .
# 
# Note: There is only one duplicate odd number
# 
# <b> Ex [1,4,6,3,1] should return 1 </b>

# In[27]:


def dup_odd_num(num):
    count=0
    dic={}
    for i in range(len(num)):
        if num[i] % 2 != 0:
            dic[0]=count
            dic[1]=num[i]
            count+=1
    return dic[1]


# In[28]:


print(dup_odd_num([3,4,6,8,]))


# In[ ]:





# In[ ]:




