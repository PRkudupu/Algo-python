#!/usr/bin/env python
# coding: utf-8

# ## Given a string containing just the characters '(', ')', '{', '}', '[' and ']', 
# ## determine if the input string is valid.
# 
# An input string is valid if:
# 
# Open brackets must be closed by the same type of brackets.
# 
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.
# 
# <b>Example 1:</b>
# 
# Input: "()"
# Output: true
# 
# <b>Example 2:</b>
# 
# Input: "()[]{}"
# Output: true
# 
# <b>Example 3:</b>
# 
# Input: "(]"
# Output: false
# 
# <b>Example 4:</b>
# 
# Input: "([)]"
# Output: false
# 
# <b>Example 5:</b>
# 
# Input: "{[]}"
# 
# <b>Output: true</b>

# #### Simple Python solution with stack

# In[2]:


def is_valid_parentheses(s):
    stack = []
    dict = {"]":"[", "}":"{", ")":"("}
    count =0
    for char in s:
        count+=1
        if char in dict.values():
            stack.append(char)
        elif char in dict.keys():
            if stack == [] or dict[char] != stack.pop():
                return False
        else:
            return False
    return stack == []
is_valid_parentheses("{}")


# In[3]:


def is_valid_parentheses(s):
    stack = []
    dict = {"]":"[", "}":"{", ")":"("}
    for char in s:
        print("char {}".format(char))
        print("stack {}".format(stack))
        print("index {}".format(s.index(char)))
        if char in dict.values():
            stack.append(char)
            print("inside if char {}".format(char))
            print("inside if stack {}".format(stack))
        elif char in dict.keys():
            print("elif stack {}".format(stack))
            if stack == [] or dict[char] != stack.pop():
                print("after pop {}".format(stack))
                return False
        else:
            print("else")
            return False
    return stack == []
is_valid_parentheses("{}")


# In[5]:


def valid_param(input):
    dic ={']':'[','}':'{',')':'('}
    stack = [];
    for char in input:
        if char in dic.values():
            stack.append(char)
        elif char in dic.keys():
            if stack == [] or dic[char] != stack.pop():
                return False
        else:
            return False
    return stack == []
valid_param("(}")


# In[ ]:


stocks=[7,1,5,2,4]
   
def buy_sell_once(s):
    maxprofit=0
    #first loop
    for i in range(len(s)-1):
        for j in range(i+1,len(s)):
            if s[j] - s[i] > maxprofit:
                maxprofit=s[j] - s[i]
    return maxprofit

m=buy_sell_once(stocks)
print(m)

