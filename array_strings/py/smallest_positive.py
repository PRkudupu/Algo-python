#!/usr/bin/env python
# coding: utf-8

# ### Smallest postive number

# In[6]:


def small_p(ls):
    sm_pos=0
    for num in ls:
        if num >=0:
            if num > sm_pos:
                sm_pos=num
    return sm_pos
        
print(small_p([1,-2,2,10-20]))       


# In[ ]:




