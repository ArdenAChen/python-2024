from Movie import Movie
from MovieCollectionNode import MovieCollectionNode
from MovieCollection import MovieCollection

def test_MovieClass():
    m1 = Movie('Alive', 'Not, Yeat', 2021)
    assert m1.getRating() == None
    assert m1.getDirector() == 'NOT, YEAT'
    assert m1.getMovieName() == 'ALIVE'
    assert m1.getYear() == 2021
    assert m1.getMovieDetails() == 'ALIVE directed by YEAT NOT (2021), Rating: None'
    m2 = Movie('twizzy rich', 'yeat, noah', 2023, 10.0)
    assert m2.getMovieDetails() == 'TWIZZY RICH directed by NOAH YEAT (2023), Rating: 10.0'

def test_MovieComparisons():
    m1 = Movie('ABCD', 'Jefferson, Justin', 2020)
    m2 = Movie('ABCD', 'Jefferson, Justin', 2021)
    m3 = Movie('ABCD', 'Jefferson, James', 2020)
    m4 = Movie('ABDC', 'Jefferson, Justin', 2020)
    m5 = Movie('ABCD', 'Jefferson, Justin', 2020)

    assert m2 > m1
    assert m1 > m3
    assert m4 > m1
    assert not m1 > m5

    assert m1 < m2
    assert m3 < m1
    assert m1 < m4
    assert not m1 < m5

    assert m1 == m5

def test_MovieCollectionNode():
    m1 = Movie('Alive', 'Not, Yeat', 2021)
    m2 = Movie('twizzy rich', 'yeat, noah', 2023, 10.0)
    m3 = Movie('ABCD', 'Jefferson, Justin', 2020)
    n1 = MovieCollectionNode(m1)
    n2 = MovieCollectionNode(m2)
    assert n1.getData() == m1
    assert n2.getNext() == None
    n1.setData(m3)
    n1.setNext(n2)
    assert n1.getNext() == n2

def test_MovieCollectionConstructor():
    mc = MovieCollection()
    assert mc.head == None

def test_MovieCollectionLength():
    m1 = Movie("A", "B, C", 2000)
    m2 = Movie("D", "E, F", 2010)
    mc = MovieCollection()
    assert mc.isEmpty() == True
    assert mc.getNumberOfMovies() == 0
    mc.insertMovie(m1)
    assert mc.isEmpty() == False
    assert mc.getNumberOfMovies() == 1
    mc.insertMovie(m2)
    assert mc.isEmpty() == False
    assert mc.getNumberOfMovies() == 2
    mc.removeDirector("B, C")
    assert mc.isEmpty() == False
    assert mc.getNumberOfMovies() == 1
    mc.removeDirector("E, F")
    assert mc.isEmpty() == True
    assert mc.getNumberOfMovies() == 0
    
def test_MovieCollectionInserts():
    m1 = Movie("Up 2 Me", "Smith, Noah", 2021, 9.5)
    m2 = Movie("2 Alive", "Smith, Noah", 2021)
    m3 = Movie("Lyfe", "Smith, Noah", 2022)
    m4 = Movie("AfterLyfe", "Smith, Noah", 2023)
    m5 = Movie("Eternal Atake 2", "Woods, Symere", 2024)

    mc1 = MovieCollection()
    mc2 = MovieCollection()

    mc1.insertMovie(m1)
    mc1.insertMovie(m2)
    mc1.insertMovie(m3)
    mc1.insertMovie(m4)
    mc1.insertMovie(m5)

    mc2.insertMovie(m5)
    mc2.insertMovie(m4)
    mc2.insertMovie(m3)
    mc2.insertMovie(m2)
    mc2.insertMovie(m1)

    assert mc1.getAllMoviesInCollection() == "2 ALIVE directed by NOAH SMITH (2021), Rating: None\n\
UP 2 ME directed by NOAH SMITH (2021), Rating: 9.5\n\
LYFE directed by NOAH SMITH (2022), Rating: None\n\
AFTERLYFE directed by NOAH SMITH (2023), Rating: None\n\
ETERNAL ATAKE 2 directed by SYMERE WOODS (2024), Rating: None\n"

    assert mc2.getAllMoviesInCollection() == "2 ALIVE directed by NOAH SMITH (2021), Rating: None\n\
UP 2 ME directed by NOAH SMITH (2021), Rating: 9.5\n\
LYFE directed by NOAH SMITH (2022), Rating: None\n\
AFTERLYFE directed by NOAH SMITH (2023), Rating: None\n\
ETERNAL ATAKE 2 directed by SYMERE WOODS (2024), Rating: None\n"

    assert mc1.getAllMoviesInCollection() == mc2.getAllMoviesInCollection()

    assert mc1.getMoviesByDirector("Smith, Noah") == "2 ALIVE directed by NOAH SMITH (2021), Rating: None\n\
UP 2 ME directed by NOAH SMITH (2021), Rating: 9.5\n\
LYFE directed by NOAH SMITH (2022), Rating: None\n\
AFTERLYFE directed by NOAH SMITH (2023), Rating: None\n"

    m6 = Movie("I Don't Know", "Alex, Alex", 2001)

    mc1.insertMovie(m6)
    assert mc1.getMoviesByDirector("Smith, Noah") == "2 ALIVE directed by NOAH SMITH (2021), Rating: None\n\
UP 2 ME directed by NOAH SMITH (2021), Rating: 9.5\n\
LYFE directed by NOAH SMITH (2022), Rating: None\n\
AFTERLYFE directed by NOAH SMITH (2023), Rating: None\n"

    mc1.removeDirector("Smith, Noah")
    assert mc1.getAllMoviesInCollection() == "I DON'T KNOW directed by ALEX ALEX (2001), Rating: None\n\
ETERNAL ATAKE 2 directed by SYMERE WOODS (2024), Rating: None\n"

    assert mc2.avgDirectorRating("Smith, Noah") == 9.50

def test_MovieCollectionAvgRating():
    mc3 = MovieCollection()

    m1 = Movie("Alive", "Smith, Noah", 2021, 8.0)
    m2 = Movie("4L", "Smith, Noah", 2021, 8.0)
    m3 = Movie("Up 2 Me", "Smith, Noah", 2021, 9.0)
    m4 = Movie("2 Alive", "Smith, Noah", 2022, 9.0)
    m5 = Movie("Lyfe", "Smith, Noah", 2022, 9.0)
    m6 = Movie("AfterLyfe", "Smith, Noah", 2023, 10.0)
    m7 = Movie("2093", "Smith, Noah", 2024, 10.0)
    m8 = Movie("LYFESTYLE", "Smith, Noah", 2024, 10.0)

    mc3.insertMovie(m1)
    mc3.insertMovie(m2)
    mc3.insertMovie(m3)
    mc3.insertMovie(m4)
    mc3.insertMovie(m5)
    mc3.insertMovie(m6)
    mc3.insertMovie(m7)
    mc3.insertMovie(m8)

    assert mc3.avgDirectorRating("Smith, Noah") == 9.12 # True value is 9.125, but Python rounds to closest even hundredth value

    mc4 = MovieCollection()
    assert mc4.avgDirectorRating("Smith, Noah") == None
    m9 = Movie("A", "Smith, Noah", 2000)
    m10 = Movie("A", "Smith, Noah", 2000)
    m11 = Movie("A", "Smith, Noah", 2000)
    mc4.insertMovie(m9)
    mc4.insertMovie(m10)
    mc4.insertMovie(m11)
    assert mc4.avgDirectorRating("Smith, Noah") == None
    mc4.insertMovie(m6)
    mc4.insertMovie(m7)
    mc4.insertMovie(m8)
    assert mc4.avgDirectorRating("Smith, Noah") == 10.0

def test_recursiveSearchMovie():
    mc3 = MovieCollection()

    m1 = Movie("Alive", "Smith, Noah", 2021, 8.0)
    m2 = Movie("4L", "Smith, Noah", 2021, 8.0)
    m3 = Movie("Up 2 Me", "Smith, Noah", 2021, 9.0)
    m4 = Movie("2 Alive", "Smith, Noah", 2022, 9.0)
    m5 = Movie("Lyfe", "Smith, Noah", 2022, 9.0)
    m6 = Movie("AfterLyfe", "Smith, Noah", 2023, 10.0)
    m7 = Movie("2093", "Smith, Noah", 2024, 10.0)
    m8 = Movie("LYFESTYLE", "Smith, Noah", 2024, 10.0)

    mc3.insertMovie(m1)
    mc3.insertMovie(m2)
    mc3.insertMovie(m3)
    mc3.insertMovie(m4)
    mc3.insertMovie(m5)
    mc3.insertMovie(m6)
    mc3.insertMovie(m7)
    mc3.insertMovie(m8)

    assert mc3.recursiveSearchMovie("AfterLyfE", mc3.head) == True
    assert mc3.recursiveSearchMovie("aliVE", mc3.head) == True
    assert mc3.recursiveSearchMovie("lyfestyle", mc3.head) == True
    assert mc3.recursiveSearchMovie("4L", mc3.head) == True
    assert mc3.recursiveSearchMovie("A Dangerous Lyfe", mc3.head) == False
    assert mc3.recursiveSearchMovie("2-Alive", mc3.head) == False