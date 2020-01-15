#!/usr/bin/env python
# coding: utf-8

# #### dic ={"first":1,"second":2,"third":3,"fourth":4}
# * Loop through all the keys
# * Loop through all the values 
# * Loop through keys and values using item
# * Loop through dictionary
# * Acces the items by refering its key name
# * Acces the items by refering its key name using get
# * Change values of a specific keys
# * Print all the values in dictionary
# * Add items to the existing dictionaries
# * Remove item from the dic
# * Remove last item in the list
# * Remove item using del
# * Delete dictionary
# 
# <p>Method	Description
#     clear()	   <b>Removes all the elements from the dictionary</b>
# <br>copy()	<b>Returns a copy of the dictionary</b>
# <br>fromkeys()	<b>Returns a dictionary with the specified keys and values</b>
# <br>get()	<b>Returns the value of the specified key</b>
# <br>items()	<b>Returns a list containing a tuple for each key value pair</b>
# <br>keys()	<b>Returns a list containing the dictionary's keys</b>
# <br>pop()	<b>Removes the element with the specified key</b>
# <br>popitem()	<b>Removes the last inserted key-value pair</b>
# <br>setdefault()	<b>Returns the value of the specified key. If the key does not exist: insert the key, with the specified value</b>
# <br>update()	<b>Updates the dictionary with the specified key-value pairs</b>
# <br>values()	<b>Returns a list of all the values in the dictionary</p>

# In[11]:


dic ={"first":1,"second":2,"third":3,"fourth":4}

# loop through all the keys
for keys in dic.keys():
    print("keys :",keys)
# loop through all the values 
print("\n")
for values in dic.values():
    print("values:",values)

#loop through keys and values using item
print("\nLoop throuh keys and values using item")
for x,y in dic.items():
    print(x,y)
print("\nLoop through the dictionary")
# loop through dictionary
for i in dic:
    print("keys: ",i)


# In[12]:


# Acces the items by refering its key name
print("Access values based on key ",dic["second"])
# Acces the items by refering its key name using get
print("Access values based on key using get",dic.get("second"))


# In[7]:


#Change values of a specific keys
dic["second"] = 10
print("Updated dictionaries values.",dic["second"])

#Print all the values in dictionary
print("\nPrint all the values in dictionary") 

for j in dic:
    print(dic[j])
    
print("\nCheck if key exits.") 
if "second" in dic:
    print("Exists")
else:
    print("Does not Exist")


# In[8]:


#Add items to the existing dictionaries
print("\n Add item to the exsting dic.")
dic["fourth"] = 2
print(dic)


# In[13]:


print("\nRemove item from the list.")
dic.pop("fourth")
print(dic)


# In[14]:


print("\nRemove last item in the list")
dic.popitem()
print(dic)


# In[15]:


print("\nRemove item using del")
del dic["second"]
print(dic)


# In[ ]:


#We can delete a dictionary using delete keyword
#del dictionary name

