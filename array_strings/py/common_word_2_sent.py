#!/usr/bin/env python
# coding: utf-8

# A sentence is a string of single-space separated words where each word consists only of lowercase letters.<br>
# 
# A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.<br>
# 
# Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.<br>
# 
#  
# <b>Example 1:</b><br>
# 
# Input: s1 = "this apple is sweet", s2 = "this apple is sour"<br>
# Output: ["sweet","sour"]<br>
# 
# <b>Example 2:</b><br>
# Input: s1 = "apple apple", s2 = "banana"<br>
# Output: ["banana"]

# In[1]:


def un_common_words(ls1,ls2):
    dic={}
    uncommon_word =[]
    for word in ls1.split():
        dic[word]=dic.get(word,0)+1
    for word in ls2.split():
        dic[word]=dic.get(word,0)+1
    for words in dic:
        if dic[words] >1:
            uncommon_word.append(words)
    return uncommon_word
s1="this apple is sweet"
s2="this apple is sour"
un_common_words(s1,s2)


# In[2]:


def un_common_words(ls1,ls2):
    dic={}
    uncommon_word =[]
    for word in ls1.split():
        dic[word]=dic.get(word,0)+1
    for word in ls2.split():
        dic[word]=dic.get(word,0)+1
    return [word for word in dic if dic[word] >1]
s1="this apple is sweet"
s2="this apple is sour"
un_common_words(s1,s2)


# In[ ]:




