#!/usr/bin/env python
# coding: utf-8

#  You are playing the following Bulls and Cows game with your friend: You write down a number and ask your friend to guess what the number is. Each time your friend makes a guess, you provide a hint that indicates how many digits in said guess match your secret number exactly in both digit and position (called "bulls") and how many digits match the secret number but locate in the wrong position (called "cows"). Your friend will use successive guesses and hints to eventually derive the secret number.
# 
# Write a function to return a hint according to the secret number and friend's guess, use A to indicate the bulls and B to indicate the cows. 
# 
# Please note that both secret number and friend's guess may contain duplicate digits.
# 
# <code>Example 1:
# 
# <b>Input: secret = "1807", guess = "7810"</b>
# 
# Output: "1A3B"
# </code>
# 
# Explanation: 1 bull and 3 cows. The bull is 8, the cows are 0, 1 and 7.
# Example 2:
# 
# <code>
# <b>Input: secret = "1123", guess = "0111"</b>
# 
# Output: "1A1B"
# </code>
# Explanation: The 1st 1 in friend's guess is a bull, the 2nd or 3rd 1 is a cow.
# Note: You may assume that the secret number and your friend's guess only contain digits, and their lengths are always                

# In[4]:


# Note this solution is brute force method. 
def bull_cow(sec,act):
    cow,bull,i =0,0,0
    n=len(sec)
    for i in range(n):
        if sec[i]==act[i]:
            bull+=1
        elif sec.count(act[i])>=1:
            cow+=1
    return str(bull)+'A'+str(cow)+'B'
print(bull_cow('1123','0111'))


# In[5]:


# Note this solution is brute force however it also does not solve all test cases.
def bull_cow(sec,act):
    cow,bull,i =0,0,0
    n=len(sec)
    s=set()
    for i in range(n):
        if sec[i]==act[i]:
            bull+=1
        elif sec.count(act[i])>=1:
            if act[i] not in s:
                s.add(act[i])
                cow+=1
    return str(bull)+'A'+str(cow)+'B'
print(bull_cow('1123','0111'))


# In[6]:


from collections import Counter
def bull_cow(sec,act):
    s, g = Counter(sec), Counter(act)
    a = sum(i == j for i, j in zip(sec, act))
    return '%sA%sB' % (a, sum((s & g).values()) - a)
print(bull_cow('1123','0111'))


# In[ ]:




