from imdb import Cinemagoer

def get_movie_id(movie):
    # search movie
    ia = Cinemagoer()

    movie = ia.search_movie(movie)[0]
    ID = movie.movieID
    return ID

def return_all_reviews(ID):
    """
    return all user imdb reviews
    """
    # create an instance of the Cinemagoer class
    ia = Cinemagoer()

    movie_reviews = ia.get_movie_reviews(ID)
    all_reviews = movie_reviews['data']['reviews']
    return all_reviews

def main():
    movie = "Everything Everywhere All At Once"
    ID = get_movie_id(movie)
    all_reviews = return_all_reviews(ID)
    print(all_reviews)

    # print(len(all_reviews)) #: 25

    # remove stop words
    # word frequencies
    # summary statistics - top twenty words
    # NLTK - sentiment analysis

if __name__ == "__main__":
    main()









