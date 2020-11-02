#!/usr/bin/env python
# coding: utf-8

# In[5]:


# With agumentation
def without_aug():
    c = 5
    while c !=0:
        print(c)
        c =c-1
without_aug()


# In[7]:


# With agumentation
def with_aug():
    c = 5
    while c !=0:
        print(c)
        c -=1
without_aug()


# In[9]:


# Implicit conversion
def imp():
    c= 5
    while c:
        print(c)
        c-=1
    return c
print(imp())       


# In[11]:


# Explicit conversion
def ex_imp():
    c=5
    while c !=0:
        print(c)
        c-=1
    return c
print(ex_imp())


# In[ ]:




