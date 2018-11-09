#!/usr/bin/env python
# coding: utf-8

# #### Given a word . Return if it is a palindrome
# 1) Input <b>"bob"</b> return <b>True</b>
# 
# 2) Input <b>"boib"</b> return <b>False</b>
# 

# In[5]:


def isPalindrome(s):
    if s.lower()== s[::-1].lower(): 
        return True
    else:return False
isPalindrome("bob")


# In[ ]:




