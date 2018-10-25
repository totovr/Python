class Movie:
    # This is the constructor
    def __init__(self, title, launched):
        self.title = title
        self.launched = launched
        print("The movie '{}' was created".format(self.title))

    # Redefine string
    def __str__(self):
        return "{} ({})".format(self.title, self.launched)

class Catalogue:
    #movies = []
    def __init__(self, movies = []):
        self.movies = movies

    def add_movies(self, p):
        self.movies.append(p)

    def show(self):
        for p in self.movies:
            print(p)

p = Movie("The Goodfather", 1972)
c = Catalogue([p])

c.show()
c.add_movies(Movie("The Goodfather: Part 2", 1974))
c.show()
