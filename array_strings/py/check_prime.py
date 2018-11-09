#!/usr/bin/env python
# coding: utf-8

# #### Validate if a given number is a prime number
# <b>Input </b> : 8
# 
# <b>Output</b> : False
# 
# <b>Input </b> : 7
# 
# <b>Output</b> : True
#         

# In[3]:


def check_prime(num):
    mid = int(num/2)
    for i in range(2,mid):
        if num % 2 == 0:
            return False
        else:
            return True
print(check_prime(7))


# 
