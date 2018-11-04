#!/usr/bin/env python
# coding: utf-8

# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
# 
# Note: For the purpose of this problem, we define empty string as valid palindrome.
# 
# Example 1:
# 
# Input: "A man, a plan, a canal: Panama"
# Output: true
# Example 2:
# 
# Input: "race a car"
# Output: false

# In[9]:


def isPalindrome(s):
    head,tail=0,len(s)-1
    while head < tail:
        while not s[head].isalnum():
            head+=1
        while not s[tail].isalnum():
            tail-=1
        if s[head].lower() != s[tail].lower():
            return False
        head+=1; tail-=1
    return True
isPalindrome("A man, a plan, a canal: Panama")


# In[11]:


def isPalindrome(s):
   head,tail=0,len(s)-1
   while head < tail:
       print("head {}".format(head))
       print("tail {}".format(tail))
       while head <tail and not s[head].isalnum():
           head+=1
       while head <tail and not s[tail].isalnum():
           tail-=1
       if s[head].lower() != s[tail].lower():
           return False
       head+=1; tail-=1
   return True
isPalindrome("bob bob")


# In[ ]:




