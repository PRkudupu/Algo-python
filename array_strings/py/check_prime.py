#!/usr/bin/env python
# coding: utf-8

# #### Validate if a given number is a prime number
# A prime number is a natural number greater than 1 that cannot be formed by multiplying two smaller natural numbers.
# 
# The first few prime numbers are
# <b> 2, 3, 5, 7, 11, 13, 17, 19, 23 and 29 </b>
# 
# Example
# 
# <b>Input </b> : 8
# 
# <b>Output</b> : False
# 
# <b>Input </b> : 7
# 
# <b>Output</b> : True
#         

# In[40]:


def check_prime(num):
    for i in range(2,num):
        if num % i == 0:
            return False
    return True
print(check_prime(4))


# In[ ]:




