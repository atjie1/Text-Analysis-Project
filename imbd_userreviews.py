from imdb import Cinemagoer
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download("vader_lexicon")


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
    all_reviews = movie_reviews["data"]["reviews"]
    return all_reviews


def return_review_content(ID):
    res = []
    d = return_all_reviews(ID)  # list
    for review in d:
        # print(type(review)) : dictionary
        res.append(review["content"])

    return res


def main():
    """
    Get all reviews
    """
    movie = "Everything Everywhere All At Once"
    ID = get_movie_id(movie)
    all_reviews = return_all_reviews(ID)
    # print(all_reviews)

    """
    How many reviews?
    """
    # print(len(all_reviews)) #: 25

    """
    Get reviews content in a list
    """
    content = return_review_content(ID)
    print(content)
    reviewcontent = "".join(
        content 
    ) # concatenate all comments into a single string

    """
    Clean Review Content
    """
    from eeaao_reddit import remove_stop_words
    clean_reviewcontent = remove_stop_words(reviewcontent)
    print(clean_reviewcontent)

    """
    Natural Language Processing of the whole of IMBD USER REVIEWS: 
    {'neg': 0.094, 'neu': 0.646, 'pos': 0.26, 'compound': 1.0}
    """
    from eeaao_reddit import print_sentiment_analysis
    print("The sentimentality score for IMBD USER REVEIWS: "), print_sentiment_analysis(
        clean_reviewcontent
    ) 
    




if __name__ == "__main__":
    main()
