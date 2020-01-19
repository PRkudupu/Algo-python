#!/usr/bin/env python
# coding: utf-8

# Given a sentence 
# 
# Input  : <b>"My name is Prathap."</b>
# 
# output : <b>"Prathap is name My."</b>

# In[2]:


def rev_sent(s):
    return " ".join(s.split(' ')[::-1])
print(rev_sent("my name is prathap."))


# In[1]:


def rev_sent(ls):
    words = ls.split(" ")
    head=0
    tail=len(words)-1
    while head <=tail:
        temp=words[tail]
        words[tail]=words[head]
        words[head]=temp
        head +=1
        tail -=1
    return words

print(rev_sent("my name is prathap"))


# In[ ]:




