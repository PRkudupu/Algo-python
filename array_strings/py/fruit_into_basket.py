#!/usr/bin/env python
# coding: utf-8

# n a row of trees, the i-th tree produces fruit with type tree[i].
# 
# You start at any tree of your choice, then repeatedly perform the following steps:
# 
# Add one piece of fruit from this tree to your baskets.  If you cannot, stop.
# Move to the next tree to the right of the current tree.  If there is no tree to the right, stop.
# Note that you do not have any choice after the initial choice of starting tree: you must perform step 1, then step 2, then back to step 1, then step 2, and so on until you stop.
# 
# You have two baskets, and each basket can carry any quantity of fruit, but you want each basket to only carry one type of fruit each.
# 
# What is the total amount of fruit you can collect with this procedure?
# 
#  
# 
# Example 1:
# 
# <b>Input: [1,2,1] 
# 
# Output: 3</b>
# 
# Explanation: We can collect [1,2,1].
# 
# Example 2:
# 
# <b>Input: [0,1,2,2]
# 
# Output: 3</b>
# Explanation: We can collect [1,2,2].
# If we started at the first tree, we would only collect [0, 1].
# 
# Example 3:
# <b>
# Input: [1,2,3,2,2]
# 
# Output: 4
# </b>
# 
# Explanation: We can collect [2,3,2,2].
# If we started at the first tree, we would only collect [1, 2].
# Example 4:
# 
# <b>
# Input: [3,3,3,1,2,1,1,2,3,3,4]
# 
# Output: 5
# </b>
# 
# Explanation: We can collect [1,2,1,1,2].
# If we started at the first tree or the eighth tree, we would only collect 4 fruits.
#  
# 
# Note:
# 
# 1 <= tree.length <= 40000
# 0 <= tree[i] < tree.length

# In[1]:


class Solution(object):
    def totalFruit(self, tree):
        blocks = [(k, len(list(v)))
                  for k, v in itertools.groupby(tree)]

        ans = i = 0
        while i < len(blocks):
            # We'll start our scan at block[i].
            # types : the different values of tree[i] seen
            # weight : the total number of trees represented
            #          by blocks under consideration
            types, weight = set(), 0

            # For each block from i and going forward,
            for j in xrange(i, len(blocks)):
                # Add each block to consideration
                types.add(blocks[j][0])
                weight += blocks[j][1]

                # If we have 3 types, this is not a legal subarray
                if len(types) >= 3:
                    i = j-1
                    break

                ans = max(ans, weight)

            # If we go to the last block, then stop
            else:
                break

        return ans


# In[13]:


import collections
class Solution(object):
    def totalFruit(self, tree):
        ans = i = 0
        count = collections.Counter()
        for j, x in enumerate(tree):
            count[x] += 1
            while len(count) >= 3:
                count[tree[i]] -= 1
                if count[tree[i]] == 0:
                    del count[tree[i]]
                i += 1
            ans = max(ans, j - i + 1)
        return ans


# In[16]:


test = Solution()
test.totalFruit([1,2,1])


# In[17]:


import collections
def fruit(tree):
    ans = i = 0
    count=collections.Counter()
    for j,x in enumerate(tree):
        count[x] += 1
        print(count)
        print(len(count))
        print("j",j)
        print("x",x)
        print("tree[i]",tree[i])
        while len(count) >= 3:
            print("count[tree[i]]",count[tree[i]])
            count[tree[i]] -= 1
            if count[tree[i]] == 0:
                del count[tree[i]]
            i += 1
        ans = max(ans, j - i + 1)
    return ans
                     
print(fruit([1,2,2,1]))
             
    
    


# In[ ]:




