#!/usr/bin/env python
# coding: utf-8

# In[13]:


class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None

class Linked_list:
    def __init__(self):
        self.head=Node()
    
    def append(self,data):
        cur=self.head
        new_node =Node(data)
        while cur.next!= None:
            cur=cur.next
        cur.next=new_node
    def display(self):
        cur=self.head
        array = []
        while cur.next!= None:
            cur=cur.next
            array.append(cur.data)
        print(array)
    
    def reverse(self):
        cur=self.head
        prev=None
        while cur:
            nxt= cur.next
            cur.next =prev;
            prev =cur
            cur =nxt
        self.head = prev
ll = Linked_list()
ll.append(10)
ll.append(20)
ll.append(30)
ll.display()
ll.reverse()
ll.display()


# In[ ]:




