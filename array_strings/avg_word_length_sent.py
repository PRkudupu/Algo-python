#!/usr/bin/env python
# coding: utf-8

# Find the average length of words in a sentence
# 
# Given a sentence <b>"my my my"</b>
# This should return <b> 2
# 
# 

# In[6]:


def avg(inp):
    total=0
    word=inp.split(" ")
    for i  in range(len(word)):
        total += len(word[i])
    return total / len(word)
avg("my my my")

