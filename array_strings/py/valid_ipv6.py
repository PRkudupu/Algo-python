#!/usr/bin/env python
# coding: utf-8

# * Validate hexadecimal in range (0, 2**16):<br>
# * 1. at least one and not more than 4 hexdigits in one chunk
# * 2. only hexdigits are allowed: 0-9, a-f, A-F
# 
# valid ipv6 ="18:36:F3:98:4F:9A"

# In[1]:


# Validate hexadecimal in range (0, 2**16):
# 1. at least one and not more than 4 hexdigits in one chunk
# 2. only hexdigits are allowed: 0-9, a-f, A-F
def valid_ipv4(ls):
   items=ls.split(":")
   if len(items) == 0 or len(items) >6:
       return False
   valid="0123456789abcdefABCDEF"
   for item in items:
       if len(item) == 0 or len(item) > 4 or not all(ch in valid for ch in item):
           return False
   return True
print(valid_ipv4("18:36:F3:98:4F:9A"))   

