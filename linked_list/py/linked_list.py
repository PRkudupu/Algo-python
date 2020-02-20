#!/usr/bin/env python
# coding: utf-8

# ![alt text](def_linked_List.JPG)

# ![alt text](LinkedList.JPG)

# Create node and assign a node pointer to the next pointer

# In[ ]:



#Assign node 1 pointer to the next node
node1.next_node =node2

print("node1.data {}".format(node1.data))
print("node2.data {}".format(node2.data))

print("node1.next_node {}".format(node1.next_node))
print("node2.next_node {}".format(node2.next_node))

print(node1.next_node)


# ## 1st  Approach

# In[ ]:





# In[11]:


#create a node class
class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None
#Create a linked list class
class Linked_List:
    def __init__(self):
        self.head=Node()
    
    def append(self,data):
        new_node=Node(data)
        cur=self.head
        while cur.next != None:
            cur=cur.next
        cur.next=new_node
    
    def display(self):
        cur=self.head
        elems = []
        while cur.next != None:
            cur=cur.next
            elems.append(cur.data)
        print(elems)
    
    def length(self):
        cur=self.head
        total=0
        while cur.next != None:
            cur=cur.next
            total+=1
        return total
    
    def remove(self,index):
        #check for out of bound exception
        if index > self.length():
            print ("Index out of bound.")
            return
        cur_node=self.head
        cur_index=0
        while True:
            last_node =cur_node
            cur_node =cur_node.next
            if cur_index == index:
                last_node.next = cur_node.next
                return
            cur_index+=1
                

ll =Linked_List()
ll.append(10)
ll.append(20)
ll.append(30)
ll.remove(1)
ll.length()
ll.display()


# In[ ]:


# Q1)
# Use the LinkedList class developed during lecture and add following method
# def item_at_index(n)
# This method returns the value stored in node on index n
# while counting your index, n=1 for first node


# Q2)
# Use the LinkedList class developed during lecture and add following method
# def delete_node_at_index(n)
# This method will delete the node present on index n
# while counting your index, n=1 for first node


# In[ ]:


class Node(object):

    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.size = 0

    def item_at_index(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if index < 0 or index >= self.size:
            return -1

        if self.head is None:
            return -1

        curr = self.head
        for i in range(index):
            curr = curr.next
        return curr.val

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list.
        After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        node = Node(val)
        node.next = self.head
        self.head = node

        self.size += 1

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        curr = self.head
        if curr is None:
            self.head = Node(val)
        else:
            while curr.next is not None:
                curr = curr.next
            curr.next = Node(val)

        self.size += 1

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list.
        If index equals to the length of linked list, the node will be appended to the end of linked list.
        If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        if index < 0 or index > self.size:
            return

        if index == 0:
            self.addAtHead(val)
        else:
            curr = self.head
            for i in range(index - 1):
                curr = curr.next
            node = Node(val)
            node.next = curr.next
            curr.next = node

            self.size += 1

    def delete_node_at_index(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        if index < 0 or index >= self.size:
            return

        curr = self.head
        if index == 0:
            self.head = curr.next
        else:
            for i in range(index - 1):
                curr = curr.next
            curr.next = curr.next.next

        self.size -= 1

def convert_to_number(self):
    #List for elements
    elems = []
    cur_node =self.head
    while cur_node.next!=None:
        cur_node = cur_node.next
        elems.append(cur_node.data)
    print(elems)

#Create intance of the linked list
my_list = MyLinkedList()
#Add new item
my_list.addAtHead(10)
#Add new item
my_list.addAtHead(20)
print("Item at index 0 -> {}".format(my_list.item_at_index(0)))
print("Item at index 1 -> {}".format(my_list.item_at_index(1)))
print("Delete item at index 1 -> {}".format(my_list.delete_node_at_index(1)))
print("Item at index 1 ->{}".format(my_list.item_at_index(1)))


# In[ ]:



#Data element or node would be passed to this node in the constructor
#By default it would be set to none
#This would be sub class
class node:
    def __init__(self,data=None):
        #Store the data point
        self.data = data
        #Store the pointer to the nex node
        self.next = None
#Wrapper class
class linked_list:
    def __int__(self):
        #Head node would not contain any actual data
        #Head node would not be indexible
        #Used as the place holder to allow us to point to the first node
        #First element would be of length 0
        self.head = node()
        
        #Adding new data point to the end of the current list
    def append(self,data):
        #This is the new node of the class node
        new_node = node(data)
        #Variable to look at the node that we are currently looking
        cur=self.head
        #Iterate through each node in the list.
        #We look for the node where current node =None
        while cur.next!=None:
            cur = cur.next
            #Last node is set as new node
        cur.next =new_node
    #Find the length of the list    
    def length(self):
        cur = self.head
        total = 0
        #iterate through the node
        while cur.next!=None:
            total+=1
            cur = cur.next
        return total
    #Helper function for display
    def display(self):
        #List for elements
        elems = []
        cur_node =self.head
        while cur_node.next!=None:
            cur_node = cur_node.next
            elems.append(cur_node.data)
        print(elems)


# In[ ]:


def get_item(self,index):
    """Get item at index"""
    current = self.head
    count   = 0
    
    while current != None and count <= index:
        count+=1
        current =current.get_next()
        
        if count!=index:
            print('Index out of bound')

