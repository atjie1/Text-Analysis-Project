from imdb import Cinemagoer

# create an instance of the Cinemagoer class
ia = Cinemagoer()

# search movie
movie = ia.search_movie("Everything Everywhere All At Once")[0]
print(movie.movieID)
#

movie_reviews = ia.get_movie_reviews('6710474')
print(movie_reviews['data']['reviews'][0]['content'])