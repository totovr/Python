
# coding: utf-8

# In[6]:


""" Example of structure programation """

clients = [
    {"Name": "Antonio", "Last name": "Vega", "DNI": "22021992"},
    {"Name": "Alex", "Last name": "Vega", "DNI": "11042005"}
]
   


# In[7]:


clients[0]["Name"]


# In[8]:


def show_client(clients, DNI):
    for c in clients:
        if(DNI == c['DNI']):
            print("{} {}".format(c["Name"], c["Last name"]))
            return
        
    print("client not found")


# In[9]:


show_client(clients, "22021992")


# In[10]:


def erase_client(clients, DNI):
    for i, c in enumerate(clients):
        if(DNI == c['DNI']):
            del(clients[i])
            print("The user {} {} was delate".format(c["Name"], c["Last name"]))
            return
    print("client not found")


# In[11]:


erase_client(clients, "22021992")


# <div class="pagebreak"></div>

# <div class="pagebreak"></div>

# <div class="pagebreak"></div>

# In[15]:


class Client:
    
    def __init__(self, dni, name, lastName):
        self.dni = dni
        self.nombre = name
        self.apellidos = lastName
        
    def __str__(self):
        return '{} {}'.format(self.name,self.lastName)
    

class Company:
    
    def __init__(self, clients=[]):
        self.clients = clients
        
    def mostrar_cliente(self, dni=None):
        for c in self.clients:
            if c.dni == dni:
                print(c)
                return
        print("The user was not found")
    
    def borrar_cliente(self, dni=None):
        for i,c in enumerate(self.clients):
            if c.dni == dni:
                del(self.clients[i])
                print(str(c),"> ERASED")
                return
        print("Client not found")


# In[16]:


Tono = Client(22021992, "Antonio", "Vega")


# In[17]:


Tono

