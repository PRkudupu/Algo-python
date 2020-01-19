#!/usr/bin/env python
# coding: utf-8

# ### Smallest postive number

# In[4]:


# smallest positive number
def sm_num(ls):
    sm=ls[0]
    for i in ls:
        if i >=0:
            sm=min(sm,i)
    return sm

print(sm_num([1,-2,2,10-20]))      


# In[ ]:




