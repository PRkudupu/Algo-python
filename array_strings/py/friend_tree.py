#!/usr/bin/env python
# coding: utf-8

# #### Facebook Friend Tree
# You have a 2-D array of friends like  [[A,B],[A,C],[B,D],[B,C],[R,M], [S],[P], [A]] Write a function that creates a dictionary of how many friends each person has. 
# * People can have 0 to many friends. 
# * However, there won't be repeat relationships like [A,B] and [B,A] and neither will there be more than 2 people in a relationship
# 
# <b>Solution:</b>
#  * We can use dictionary to store friends and count details
#  * We would only consider the keys and not the values for counting the no of friends. Due to no repeat relationship
#      [A,B] and [B,A]
#  * In the 2 dimensional array if there is only one entry in the rows. Then it is not considered as friends
#    To achieve this condition, we can validate the length of the item(rows) in the array -1 
#  * If there are more entries for a friend (key
#    

# In[15]:


def friend_tree(items):
    results ={} # we can also declare results = dic()
    for item in items:
        if item[0] not in results:
            results[item[0]] =len(item)-1
        elif item[0] in results:
            results[item[0]] +=len(item)-1
    return results


# In[16]:


items=[['A','B'],['A','C'],['B','D'],['B','C'],['R','M'], ['S'],['P'], ['A'],['A','E']]
print(friend_tree(items))


# In[17]:


def friend_tree(items):
    result=dict()
    count =1
    for item in items:
        print('\nresult',result)
        print('item:',item)
        print('items[0]',item[0])
        print('len(item)',len(item))
        print('len(item)',len(item)-1)
        if item[0] not in result.keys():
            result[item[0]]=len(item)-1
            print('### NOTIN')
        elif item[0] in result.keys():
            print('in')
            result[item[0]]+=len(item)-1
    return result
items=[['A','B'],['A','C'],['B','D'],['B','C'],['R','M'], ['S'],['P'], ['A'],['A','E']]

print(friend_tree(items))


# In[ ]:




