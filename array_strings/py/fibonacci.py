#!/usr/bin/env python
# coding: utf-8

# Return fibonacci element of the series ex: 1,1,2,3
# 
# <b> Input  </b> : 4
# 
# <b> Output </b> : 3

# In[8]:


def fib(n):
    a,b=1,1
    for i in range(n-1):
        a,b=b,b+a
    return a
print(fib(4))


# In[9]:


def fib(n):
    if n == 1 or n == 2: return 1
    return fib(n-1)+fib(n-2)
print(fib(4))

