#!/usr/bin/env python
# coding: utf-8

# In[1]:


def test_incr():
    s ='x'
    i=0
    while len(s) < 7:
        s +=s
        i+=1
    return i
print(test_incr())


# In[ ]:




