class Movie:

    def __init__(self, movieName, director, year, rating=None):
        self.movieName = movieName.upper()
        self.director = director.upper()
        self.year = year
        self.rating = rating
    
    def getMovieName(self):
        return self.movieName
    
    def getDirector(self):
        return self.director
    
    def getYear(self):
        return self.year
    
    def getRating(self):
        return self.rating
    
    def getMovieDetails(self):
        directorFirstLast = self.director.split()
        directorFirstLast = directorFirstLast[1] + ' ' + directorFirstLast[0][:-1]
        return f'{self.movieName} directed by {directorFirstLast} ({self.year}), Rating: {self.rating}'

    def __gt__(self, other):
        if self.director != other.director:
            return self.director > other.director
        elif self.year != other.year:
            return self.year > other.year
        else:
            return self.movieName > other.movieName
    
    def __eq__(self, other):
        return self.director == other.director and self.year == other.year and self.movieName == other.movieName
    
    def __lt__(self, other):
        if self.director != other.director:
            return self.director < other.director
        elif self.year != other.year:
            return self.year < other.year
        else:
            return self.movieName < other.movieName