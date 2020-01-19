#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def uniq(ls):
    words=ls.split()
    dic={}
    for w in words:
        if w in dic:
            continue
        else:
            dic[w]=ls.count(w)
    return dic
print(uniq("my my name prathap"))


# In[2]:


#Wecan word count from list using count as shown below
test="my my name is prathap"
print(test.count("my"))


# In[ ]:




