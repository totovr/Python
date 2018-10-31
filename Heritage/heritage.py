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
