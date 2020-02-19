#!/usr/bin/env python
# coding: utf-8

# Given a string, find the length of the longest substring without repeating characters.
# 
# Example 1:
# 
# <b>Input: "abcabcbb"</b>
# Output: 3 
# Explanation: The answer is "abc", with the length of 3. 
# Example 2:
# 
# <b>Input: "bbbbb"</b>
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:
# 
# <b>Input: "pwwkew"</b>
# Output: 3
# Explanation: The answer is "wke", with the length of 3. 
#              Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

# ![](images/longsub)

# In[16]:


#BRUTEFORCE
def long_sub_string(ls):
    sub_set =""
    dic ={}
    s = set()
    maxi=0
    for i in ls:
        if i not in s:
            s.add(i)
            sub_set =sub_set+i
        else:
            dic[sub_set]=len(sub_set)
            sub_set =""
            sub_set =sub_set+i
            s=set()
            s.add(i)
        dic[sub_set]=len(sub_set)
        maxi=max(maxi,dic[sub_set])
    return maxi
print(long_sub_string('pwwkew'))


# ![title](image/longsub.jpg)

# In[2]:


def lengthOfLongestSubstring(s):
        start = maxLength = 0
        dic = {}
        
        for i in range(len(s)):
            if s[i] in dic and start <= dic[s[i]]:
                start = dic[s[i]] + 1
            else:
                # Here i-strat is where we are removing the index from previous sub string
                # +1 is added as index starts from 0
                maxLength = max(maxLength, i - start + 1)

            dic[s[i]] = i

        return maxLength
print(lengthOfLongestSubstring('abcdakujgbna'))


# In[18]:


#WITH PRINT
def len_longest_sub(ls):
    #start is used to track new substring. We increement start when duplicate is found
    start = maxLength = 0
    dic = {}
    for i in range(len(ls)):
        if ls[i] in dic and start <= dic[ls[i]]:
            print("if")
            start = dic[ls[i]] + 1
        else:
            print("else")
            # I is the current pointer and start is the previous sub string.
            # since i starts from 0 we need to increement by 1
            maxLength = max(maxLength, i - start + 1)
        dic[ls[i]] = i
        print("\ni ->",i)
        print("start <= dic[ls[i]]",start ,dic[ls[i]])
        print("dic ->",dic)
        print("maxlength",maxLength)
    return maxLength
print(len_longest_sub("abadbc"))


# In[ ]:




