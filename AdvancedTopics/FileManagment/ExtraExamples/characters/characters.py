from io import open
import pickle

class Character:
    
    def __init__(self, cT, cL, cA, cD, cR):
        self.cT = cT
        self.cL = cL
        self.cA = cA
        self.cD = cD
        self.cR = cR

    def __str__(self):
        return "The {} has {} points of life, {} of attack, {} of defense and {} of range ".format(
        self.cT, self.cL, self.cA, self.cD, self.cR)

class Manager:
    
    characterL = []

    def __init__(self):
        self.load()

    def add_character(self, p):

        for cTemp in self.characterL:
            if cTemp.cT == p.cT:
                return
        self.characterL.append(p)
        self.save()

    def show(self):
        if len(self.characterL) == 0:
            print("There are not characters in the game")
        else:
            for p in self.characterL:
                print(p)

    def load(self):
        file = open('game.pckl', 'ab+') # binary append with lecture mode
        file.seek(0)
        try:
            self.characterL = pickle.load(file)
        except:
            print("This file is empty") # if the file is empty 
        finally:
            file.close()
            print("{} characters were loaded".format(len(self.characterL)))
    
    def save(self):
        file = open('game.pckl', 'wb+')
        pickle.dump(self.characterL, file)
        file.close()

    # Destroy the class
    def __del__(self):
        self.save() # automatic save
        print("The catalogue was saved")

# Create the manager
c = Manager()
# show the content
c.show()
# Add the movies
c.add_character( Character("Caballero",4,2,4,2) )
c.add_character( Character("Caballero",4,2,4,2) )
# Show again the catalogue
c.show()
# Delate the catalogue of the ram memory, the file will persist in the folder
del(c)