#!/usr/bin/env python
# coding: utf-8

# In[2]:


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

