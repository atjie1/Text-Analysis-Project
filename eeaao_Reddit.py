# 3/12 The Day of the Oscars

import praw
from config import client_id, client_secret, username, password, user_agent
import pickle

def open_comments(URL):
    """
    returns top_level_comments from a reddit URL post/submission
    """
    reddit = praw.Reddit(
        client_id=client_id,
        client_secret=client_secret,
        username=username,
        password=password,
        user_agent=user_agent,
    )

    # sub = "movies"
    # submissions = reddit.subreddit(sub).top(time_filter="all", limit=5)
    # top5 = [(submission.title, submission.selftext) for submission in submissions]
    # print(top5)   

    submission = reddit.submission(url=URL[0]) # https://praw.readthedocs.io/en/stable/code_overview/models/comment.html 
    top_level_comments = list(submission.comments)
    return top_level_comments

def print_comments(URL):
    """
    returns top_level_comments from a reddit URL post/submission
    """
    top_level_comments = open_comments(URL)
    for comment in top_level_comments:
        print(comment.body)

def count_comments(URL):
    top_level_comments = open_comments(URL)
    print(len(top_level_comments))

def main():
    URL1 = [
    'https://www.reddit.com/r/flicks/comments/uex2hv/lets_talk_about_everything_everywhere_all_at_once/',
    ]

    URL2 = [
        'https://www.reddit.com/r/movies/comments/11pjwko/not_getting_the_hype_for_everything_everywhere/'
    ]

    # print_comments(URL1) # Before oscars
    # count_comments(URL1) #17 comments

    # print_comments(URL2) # After oscars
    # count_comments(URL1) #166 comments    
    
    # remove stop words
    # word frequencies
    # summary statistics - top twenty words
    # NLTK - sentiment analysis
    # Text clustering of two reddit submissions
    

if __name__ == "__main__":
    main()