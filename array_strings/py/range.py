#!/usr/bin/env python
# coding: utf-8

# In[15]:


a = [3,6,7]
# First arg for range is start, stop and step, default is 1
# Decreement. We need the index so we need to have len(a)-1
print('length',len(a))
print('length-1',len(a)-1)
for i in range(len(a)-1,-1,-1):
    print(a[i])
    


# In[16]:


a = [3,6,7]
# First arg for range is start, stop and step, default is 1
# Increement
for i in range(0,len(a),1):
    print(a[i])


# In[18]:


#Extended slicing
a = [3,6,7]
for i in a[::-1]:
    print(i)


# In[ ]:




