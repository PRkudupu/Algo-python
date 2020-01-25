#!/usr/bin/env python
# coding: utf-8

# String to Integer (atoi)
# Implement atoi which converts a string to an integer.
# 
# The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.
# 
# The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.
# 
# If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.
# 
# If no valid conversion could be performed, a zero value is returned.
# 
# Note:
# 
# Only the space character ' ' is considered as whitespace character.
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.
# 

# <b>Example 1:</b>
# 
# Input: "42"
# Output: 42
# 
# 

# <b>Example 2:</b>
# 
# Input: "   -42"
# Output: -42
# Explanation: The first non-whitespace character is '-', which is the minus sign.
#              Then take as many numerical digits as possible, which gets 42.
# 

# <b>Example 3:</b>
# 
# Input: "4193 with words"
# Output: 4193
# Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.
# 

# <b>Example 4:</b>
# 
# Input: "words and 987"
# Output: 0
# Explanation: The first non-whitespace character is 'w', which is not a numerical 
#              digit or a +/- sign. Therefore no valid conversion could be performed.
# 

# <b>Example 5:</b>
# 
# Input: "-91283472332"
# Output: -2147483648
# Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
#              Thefore INT_MIN (−231) is returned.

# In[7]:


# remove white space from begining and end using strip
# Have a dictionary of valid numberical numbers validate if the ch is numerical using isdigit
# store the new character in a varible
# Run a convert function from int

def str_int(ls):
    var =""
    for ch in ls.strip():
        # Check if the ch is digit or ch is a negative character
        if ch.isdigit() or ch == "-":
            var +=ch
    # if int is not a 32 bit integer
    if (int(var)>>32):
        var =-2147483648
    return int(var)
print(str_int('  4193 with words'))
print(str_int('42'))
print(str_int('-42'))
print(str_int('4193 with words'))
print(str_int('words and 987'))
print(str_int('-91283472332'))


# In[ ]:




