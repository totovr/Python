# Father class
class Product:
    def __init__(self, reference, name, pfp, description):
        self.reference = reference
        self.name = name
        self.pfp = pfp
        self.description = description

    def __str__(self):
        return """\
        REFERENCE \t{}
        NAME \t\t{}
        PfP \t\t{}
        DESCRIPTION \t{}""".format(self.reference,self.name,self.pfp,self.description)

# Son class

class Ornament(Product):
    pass

class Food(Product):

    productor = ""
    distribuitor = ""

    def __str__(self):
        return """\
        REFERENCE \t{}
        NAME \t\t{}
        PfP \t\t{}
        DESCRIPTION \t{}
        PRODUCTOR \t{}
        DISTRIBUITOR \t{}""".format(self.reference,self.name,self.pfp,self.description,self.productor,self.distribuitor)

# Son class
class Book(Product):

    isbn = ""
    author = ""

    def __str__(self):
        return """\
        REFERENCE \t{}
        NAME \t\t{}
        PfP \t\t{}
        DESCRIPTION \t{}
        PRODUCTOR \t{}
        DISTRIBUITOR \t{}""".format(self.reference,self.name,self.pfp,self.description,self.isbn,self.author)

# Elements

o = Ornament(2020,"Glass with pictures",10,"Animal print")

f = Food('000A','Oil',15,'Olive oil')
f.productor = "The happy oiler"
f.distribuitor = "Costco"

b = Book('000A','Rich Japanese Food',20,'Cook book')
b.isbn = "a1029343"
b.author = "The chefchef"

# List of the products
products = [o,f]
products.append(b)

products

for p in products:
    print(p, "\n")

for p in products:
    print(p.reference,p.name)

# This is an error because not all the class has the same intances
for p in products:
    print(p.author)

# This method is to check if an object is of the type that is evaluating
for p in products:
    if( isinstance(p, Ornament) ):
        print(p.reference,p.name)
    elif( isinstance(p, Food) ):
        print(p.reference,p.name,p.productor)
    elif( isinstance(p, Book) ):
        print(p.reference,p.name,p.isbn)

# The p variable is a local variable
def discount_product(p, discount):
    """ Give discount of a product that is in the list"""
    p.pfp = p.pfp - (p.pfp/100 * discount)
    return p

# food type
p_discount = discount_product(f, 10)
print(p_discount)

# Method to copy one object
import copy

copy_o = copy.copy(o)
print(o)
copy_o.pfp = 15
print(copy_o)
