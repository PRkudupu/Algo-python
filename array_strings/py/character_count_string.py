#!/usr/bin/env python
# coding: utf-8

# In[1]:


def count_sip(ls,k):
    if ls == None:
        return None
    if len(ls) == 0:
        return []
    if len(ls) <4:
        return 'Length less than 4'
    count =0
    for ch in ls:
        if k == ch:
            count +=1
    return count

print(count_sip(None,'s'))
print(count_sip([],'s'))
print(count_sip('mis','s'))
print(count_sip('missisipi','s'))


# In[ ]:




