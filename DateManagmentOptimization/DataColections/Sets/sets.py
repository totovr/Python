
# coding: utf-8

# In[1]:


# The set has not order
setExample = set()
setExample
setExample = {1, 2, 3}


# In[2]:


setExample


# In[3]:


setExample.add(4)
setExample.add(0)
setExample


# In[4]:


setExample.add('H')
setExample


# In[5]:


# The set class will order the elements
setExample.add('A')
setExample.add('Z')
setExample


# In[6]:


group = {'Tono', 'John', 'Pol'}


# In[9]:


'Tono' in group


# In[10]:


'Cindy' in group


# In[8]:


'Tono' not in group


# In[11]:


test = {'Hector', 'Hector', 'Hector'}


# In[12]:


test


# In[14]:


l = [1, 2, 3, 3, 2, 1]
l


# In[15]:


c = set(l)


# In[16]:


c


# In[17]:


l = list(c)


# In[18]:


l


# In[19]:


l = [1, 2, 3, 3, 2, 1]


# In[20]:


l = list( set(l))


# In[21]:


l


# In[22]:


s = "I ate tacos"


# In[23]:


set(s)

