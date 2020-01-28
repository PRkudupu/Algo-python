#!/usr/bin/env python
# coding: utf-8

# ### Multiply Strings
# ![alt text](image/multiply_strings.JPG)

# In[1]:


# mutliply strings
"""The length of both num1 and num2 is < 110.
Both num1 and num2 contain only digits 0-9.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
You must not use any built-in BigInteger library or convert the inputs to integer directly."""
def mul(num1,num2):
    result=0
    if len(num1) >110 or len(num2) > 110:
        return "less than 110"
    elif not num1.isdigit() or not num2.isdigit():
        return "not a digit."
    for i in range(0,int(num2)):
        result += int(num1)
    return result
print(mul('20','5'))
        


# In[ ]:




