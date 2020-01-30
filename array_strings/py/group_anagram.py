#!/usr/bin/env python
# coding: utf-8

# ## Group Anagram
# ![alt text](image/group_anagram.JPG)

# ### Solution: Approach 1
# <pre>Maintain a map ans : {String -> List} where each key \text{K}K is a sorted string, and each value is the list of strings from the initial input that when sorted, are equal to \text{K}K.</pre>
# 
# <b>store the key as a hashable tuple, eg. ('c', 'o', 'd', 'e')</b>
# ![alt text](image/gpan.JPG)
# Complexity Analysis
# 
# <b>Time Complexity:</b> O(NK \log K)O(NKlogK), where NN is the length of strs, and KK is the maximum length of a string in strs. The outer loop has complexity O(N)O(N) as we iterate through each string. Then, we sort each string in O(K \log K)O(KlogK) time.
# 
# Space Complexity: O(NK)O(NK), the total information content stored in ans

# In[9]:


#WITH COMMENTS AND PRINT
import collections
def anagram(ls):
#defaultdict means that if a key is not found in the dictionary, then instead of a KeyError being thrown, a new entry is created
    ans = collections.defaultdict(list)
    for s in ls:
        ans[tuple(sorted(s))].append(s)
        print("\ns:",s)
        print("ans:",ans)
    return ans.values()
print(anagram(["eat", "tea", "tan", "ate", "nat", "bat"]))


# ### Approach 2: Categorize by Count
# Intuition
# 
# Two strings are anagrams if and only if their character counts (respective number of occurrences of each character) are the same.
# 
# We can transform each string \text{s}s into a character count, \text{count}count, consisting of 26 non-negative integers representing the number of \text{a}a's, \text{b}b's, \text{c}c's, etc. We use these counts as the basis for our hash map.
# 
# In python, the representation will be a tuple of the counts. For example, abbccc will be (1, 2, 3, 0, 0, ..., 0), where again there are 26 entries total.
# 
# ![alt text](image/gp_ans.JPG)
# ex:
# {(1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0): ['eat']})
# c e
# <b>Complexity Analysis</b>
# 
# Time Complexity: O(NK)O(NK), where NN is the length of strs, and KK is the maximum length of a string in strs. Counting each string is linear in the size of the string, and we count every string.
# 
# Space Complexity: O(NK)O(NK), the total information content stored in ans.

# In[10]:


def groupAnagrams(strs):
       ans = collections.defaultdict(list)
       for s in strs:
           count = [0] * 26
           for c in s:
               count[ord(c) - ord('a')] += 1
           ans[tuple(count)].append(s)
       return ans.values()
print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))


# In[ ]:




