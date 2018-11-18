from io import open
import pickle

class Character:
    
    def __init__(self, cType, cLife, cAttack, cDefense, cRange):
        self.cType = cType
        self.cLife = cLife
        self.cAttack = cAttack
        self.cDefense = cDefense
        self.cRange = cRange
    
    def __str__(self):
        return "The {} has {} of life, {} of attack, {} of defense and {} of range".format(
            self.cType, self.cLife, self.cAttack, self.cDefense, self.cRange)

class Manager:
    
    charactersL = []
    def __init__(self):
        self.load()
    
    # Load the file 
    def load(self):
        file = open('catalogue.pckl', 'ab+') # binary append with lecture mode
        file.seek(0)
        try:
            self.charactersL = pickle.load(file)
        except:
            print("This file is empty") # if the file is empty 
        finally:
            file.close()
            print("{} characters were loaded".format(len(self.charactersL)))

    def add_characters(self, p):
        for characterTemp in self.charactersL: # loop all the character list
            if characterTemp.Type == p.Type: # check if the type is in the object list
                return 
        # If the character is not in the list it will be add
        self.charactersL.append(p)
        self.save()

    def show(self):
        if len(self.charactersL) == 0:
            print("There are not characters in the catalogue")
        else:
            for p in self.charactersL:
                print(p)
    
    def save(self):
        file = open('catalogue.pckl', 'wb+')
        pickle.dump(self.charactersL, file)
        file.close()

    # Destroy the class
    def __del__(self):
        self.save() # automatic save
        print("The catalogue was saved")

