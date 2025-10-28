from Movie import Movie
from MovieCollectionNode import MovieCollectionNode

class MovieCollection:
    def __init__(self):
        self.head = None
    
    def isEmpty(self):
        return self.head == None
    
    def getNumberOfMovies(self):
        temp = self.head
        count = 0
        while temp != None:
            count = count + 1
            temp = temp.getNext()
        return count

    def insertMovie(self, movie):
        current = self.head
        previous = None
        stop = False

        # find the correct place in the list to insert movie
        while current != None and not stop:
            if current.getData() > movie:
                stop = True
            else:
                previous = current
                current = current.getNext()
        
        # Create node with movie to add
        temp = MovieCollectionNode(movie)

        # Case 1: insert at front of the list
        if previous == None:
            temp.setNext(self.head)
            self.head = temp

        # Case 2: insert not at front
        else:
            temp.setNext(current)
            previous.setNext(temp)
        
    def getAllMoviesInCollection(self):
        current = self.head
        output = ""
        while current != None:
            output += current.getData().getMovieDetails()
            output += '\n'
            current = current.getNext()
        return output
    
    def getMoviesByDirector(self, director):
        current = self.head
        output = ""
        while current != None:
            if current.getData().director == director.upper():
                output += current.getData().getMovieDetails()
                output += '\n'
            current = current.getNext()
        return output

    def removeDirector(self, director):
        current = self.head
        previous = None

        while current != None:
            if current.getData().director == director.upper():
                if previous == None:
                    self.head = current.getNext()
                else:
                    previous.setNext(current.getNext())
                current = current.getNext()
            else:
                previous = current
                current = current.getNext()

    def avgDirectorRating(self, director):
        current = self.head
        total_rating = 0
        count = 0

        while current != None:
            movie = current.getData()
            
            if movie.director == director.upper() and movie.getRating() != None:
                total_rating += movie.getRating()
                count += 1

            current = current.getNext()

        if count == 0: # If no movies w/ ratings by director, return None
            return None
        
        average_rating = round(total_rating / count, 2)
        return average_rating

    def recursiveSearchMovie(self, movieName, movieNode):
        if movieNode == None:
            return False
        
        if movieNode.getData().movieName == movieName.upper():
            return True
        
        return self.recursiveSearchMovie(movieName, movieNode.getNext())