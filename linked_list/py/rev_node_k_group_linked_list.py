#!/usr/bin/env python
# coding: utf-8

# Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
# 
# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.
# 
# <b>Example</b>:
# 
# Given this linked list: 1->2->3->4->5
# 
# For k = 2, you should return: 2->1->4->3->5
# 
# For k = 3, you should return: 3->2->1->4->5
# 
# Note:
# 
# Only constant extra memory is allowed.
# You may not alter the values in the list's nodes, only nodes itself may be changed.

# In[1]:


class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None
        
class Linked_list:
    def __init__(self):
        self.head=Node()
    
    def append(self,data):
        cur=self.head
        new_node=Node(data)
        while cur.next != None:
            cur=cur.next
        cur.next=new_node
    
    def display(self):
        cur=self.head
        array =[]
        while cur.next != None:
            cur=cur.next
            array.append(cur.data)
        print(array)
    
    def kth_from_last(self,k):
            self.reverse()
            cur=self.head
            prev=None
            count=1
            while cur:
                cur=cur.next
                if k == count:
                    return cur.data
                count+=1


# In[9]:


ll = Linked_list()
ll.append(10)
ll.append(20)
ll.append(5)
ll.append(30)
ll.display()
new_list=ll.kth_from_last(2)


# In[ ]:




