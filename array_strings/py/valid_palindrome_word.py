#!/usr/bin/env python
# coding: utf-8

# #### Given a word . Return if it is a palindrome
# 1) Input <b>"bob"</b> return <b>True</b>
# 
# 2) Input <b>"boib"</b> return <b>False</b>
# 

# In[2]:


def isPalindrome(s):
    if s.lower()== s[::-1].lower(): 
        return True
    else:return False
isPalindrome("bob")


# In[4]:


def valid_palindrome(input):
    first =0
    last =len(input)
    while first <=last:
        if input[first].lower() != input[last-1].lower():
            return False
        first +=1
        last -=1
    return True
valid_palindrome("boB")
   


# In[ ]:




