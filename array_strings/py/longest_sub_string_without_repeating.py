#!/usr/bin/env python
# coding: utf-8

# Given a string, find the length of the longest substring without repeating characters.
# 
# Example 1:
# 
# Input: "abcabcbb"
# Output: 3 
# Explanation: The answer is "abc", with the length of 3. 
# Example 2:
# 
# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:
# 
# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3. 
#              Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

# In[12]:


def long_sub_string(ls):
    sub_set =""
    dic ={}
    s = set()
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
    for y in dic.values():
        maxi=0
        return max(maxi,y)
    return dic
print(long_sub_string('abcdabc'))


# In[13]:


def lengthOfLongestSubstring(s):
        start = maxLength = 0
        usedChar = {}
        
        for i in range(len(s)):
            if s[i] in usedChar and start <= usedChar[s[i]]:
                start = usedChar[s[i]] + 1
            else:
                maxLength = max(maxLength, i - start + 1)

            usedChar[s[i]] = i

        return maxLength
print(lengthOfLongestSubstring('abcdabc'))


# In[1]:


def len_longest_sub(ls):
    start = maxLength = 0
    dic = {}
    for i in range(len(ls)):
        if ls[i] in dic and start <= dic[ls[i]]:
            print("if")
            start = dic[ls[i]] + 1
        else:
            print("else")
            maxLength = max(maxLength, i - start + 1)
        dic[ls[i]] = i
        print("\ni ->",i)
        print("ls[i]",ls[i])
        print("start ->",start)
        print("dic[ls[i]] ->",dic[ls[i]])
        print("dic ->",dic)
        print("maxlength",maxLength)
    return maxLength
print(len_longest_sub("ababcabcd"))


# In[ ]:




