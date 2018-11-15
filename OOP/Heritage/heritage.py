class Product:
    def __init__(self, reference, type, name, pfp, description, productor = None, distribuitor = None, isbn = None, author = None):
        self.reference = reference
        self.type = type
        self.name = name
        self.pfp = pfp
        self.description = description
        self.productor = productor
        self.distribuitor = distribuitor
        self.isbn = isbn
        self.author = author

ornament = Product('000A','ornament','glass',15,'glass with draws')
ornament.type

# Because we have 3 kind of different products we have to define a father class and son class
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

class Ornament(Product):
    pass

o = Ornament('000A','Ornament',15,'Glass with cool draws')
print(o)

# Son class
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

f = Food('000A','Oil',15,'Olive oil')
f.productor = "The happy oiler"
f.distribuitor = "Costco"
print(f)

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

b = Book('000A','Rich Japanese Food',20,'Cook book')
b.isbn = "a1029343"
b.author = "The chefchef"
print(b)
