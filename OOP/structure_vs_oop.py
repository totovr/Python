
# coding: utf-8

# In[1]:


""" Example of structure programation """

clients = [
    {"Name": "Antonio", "Last name": "Vega", "DNI": "22021992"},
    {"Name": "Alex", "Last name": "Vega", "DNI": "11042005"}
]
   


# In[2]:


clients[0]["Name"]


# In[3]:


def show_client(clients, DNI):
    for c in clients:
        if(DNI == c['DNI']):
            print("{} {}".format(c["Name"], c["Last name"]))
            return
        
    print("client not found")


# In[4]:


show_client(clients, "22021992")


# In[5]:


def erase_client(clients, DNI):
    for i, c in enumerate(clients):
        if(DNI == c['DNI']):
            del(clients[i])
            print("The user {} {} was delate".format(c["Name"], c["Last name"]))
            return
    print("client not found")


# In[6]:


erase_client(clients, "22021992")


# <div class="pagebreak"></div>

# <div class="pagebreak"></div>

# <div class="pagebreak"></div>

# # This is an example of a Class

# In[38]:


class Client:
    
    def __init__(self, DNI, name, lastName):
        self.DNI = DNI
        self.name = name
        self.lastName = lastName
        
    def __str__(self):
        return '{} {}'.format(self.name,self.lastName)
    

class Company:
    
    def __init__(self, clients=[]):
        self.clients = clients
        
    def show_clients(self, DNI=None):
        for c in self.clients:
            if c.DNI == DNI:
                print(c)
                return
        print("The user was not found")
    
    def erase_client(self, DNI = None):
        for i,c in enumerate(self.clients):
            if c.DNI == DNI:
                del(self.clients[i])
                print(str(c),"> ERASED")
                return
        print("Client not found")


# In[39]:


Tono = Client(22021992, "Antonio", "Vega")


# In[40]:


Tono


# In[41]:


Alex = Client("11042005", "Alexandro", "Vega")


# In[42]:


Alex


# In[43]:


company = Company(clients = [Tono, Alex])


# In[44]:


company.clients


# In[45]:


company.show_clients(DNI = "11042005")


# In[46]:


company.erase_client(DNI = "11042005")


# In[47]:


company.clients

