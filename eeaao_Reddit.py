# 3/12 The Day of the Oscars

import praw
from config import client_id, client_secret, username, password, user_agent
import emoji
import nltk

nltk.download('stopwords')
from nltk.corpus import stopwords #ChatGPT
stop_words = set(stopwords.words('english'))

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

def comments(URL):
    """
    returns list of top level comments from a reddit URL post/submission
    """
    top_level_comments = open_comments(URL)
    comment_list = []
    for comment in top_level_comments:
        comment = comment.body
        comment_list.append(comment)
    return comment_list

def count_comments(URL):
    top_level_comments = open_comments(URL)
    print(len(top_level_comments))

def extract_emojis(text): #You can use the emoji library. You can check if a single codepoint is an emoji codepoint by checking if it is contained in emoji.UNICODE_EMOJI.
    emojis = []
    unicodeemoji_dict = emoji.get_emoji_unicode_dict('en') #':man_surfing_medium-light_skin_tone:': '🏄🏼\u200d♂️', ':man_surfing_medium_skin_tone:': '🏄🏽\u200d♂️'...
    unicodeemoji = list(unicodeemoji_dict.values()) #'🍽️', '🥠', '⛲', '🖋️', '🕟', '🍀', '🕓', '  🦊', '🖼️', '🍟', '🍤', '🐸', '🐥', '☹️'
    for char in text:
        if char in unicodeemoji:
            emojis.append(char)
    return emojis
        
def remove_stop_words(text):
    """
    remove stopwords and emojis
    """
    # Replace dashes and em dashes with spaces
    text = text.replace("-", " ")
    text = text.replace(chr(8212), " ") # Unicode 8212 is the HTML decimal entity for em dash
    
    # Remove punctuation
    # text = text.translate(str.maketrans('','', string.punctuation))
    text = text.replace("."," ")
    text = text.replace("!", " ")
    text = text.replace("?", " ")

    
    # Make lowercase
    text = text.lower()

    # Remove emojis
    emojis = extract_emojis(text)
    for emoji in emojis:
        text = text.replace(emoji, " ")

    # Remove stop words
    words = text.split()
    word_list = []
    for word in words:
        if word not in stop_words:
            word_list.append(word + " ")
    text = ''.join(word_list)

    return text

def process_text(text):
    """
    Makes a sorted histogram dictionary that contains the words from a text with value as the number of times it appears
    """
    hist = {}

    for word in text.split():
        hist[word] = hist.get(word,0) + 1

    sorted_hist = dict(sorted(hist.items(), key=lambda item:item[1], reverse=True))
    
    return sorted_hist

def print_histogram_list(dictionary, x):
    """
    Takes dictionary and prints a list of x length of items and values
    """
    histogram_list = list(dictionary.items())
    for key, value in histogram_list[:x]:
        print(key, value)

def different_words(dictionary):
    """
    Returns the number of different words in a dictionary.
    """
    return len(dictionary)

def subtract(d1, d2):
    """
    Returns a dictionary with all keys that appear in d1 but not d2.
    """
    res = dict()
    for word in d1:
        if word in d2:
            res[word] = res.get(word,0)

    return res

def main():

    URL1 = [
        'https://www.reddit.com/r/flicks/comments/uex2hv/lets_talk_about_everything_everywhere_all_at_once/',
    ]

    """
    Convert to Text
    """
    URL1_comments = comments(URL1) # comment list before oscars, just comment body, not IDs
    count_comments(URL1) # 17 comments
    URL1_text = ''.join(URL1_comments) # concatenate all comments into a single string (CHATGPT)
    print("URL1 Text:" , URL1_text)
    
    """
    Extract Emojis: NONE
    """
    emojis1 = extract_emojis(URL1_text)
    print("URL1 Emojis:", emojis1)

    """
    Clean Text: remove hyphens, punctuation, emojis, stopwords according to NLTK, make lowercase
    """
    clean_text1 = remove_stop_words(URL1_text)
    print("URL CLeaned Text1: ", clean_text1)

    """
    Find Top 50 Words and Frequency
    """
    histogram1 = process_text(clean_text1)
    print_histogram_list(histogram1,50)

    """
    Set of Words: 557 words
    """
    print(different_words(histogram1))

    URL2 = [
        'https://www.reddit.com/r/movies/comments/11pjwko/not_getting_the_hype_for_everything_everywhere/'
    ]

    """
    Convert to Text
    """
    URL2_comments = comments(URL2)
    print(comments(URL2)) # print comment list after oscars, just comment body, not IDs
    count_comments(URL1) # 166 comments
    URL2_text = ''.join(URL2_comments) # concatenate all comments into a single string (CHATGPT)
    print("URL Text:", URL2_text)

    """
    Extract Emojis: "URL2 Emojis: ['🤞', '👎', '😭']"
    """
    emojis2 = extract_emojis(URL2_text)
    print("URL2 Emojis:", emojis2) # no emojis

    """
    Clean Text: remove hyphens, punctuation, emojis, stopwords according to NLTK, make lowercase
    """
    clean_text2 = remove_stop_words(URL2_text)
    print("URL CLeaned Text2: ", clean_text2)

    """
    Find Top Frequency and Top 50 Words 
    """
    histogram2 = process_text(clean_text2)
    print_histogram_list(histogram2,50)

    """
    Set of Words: 2123 words
    """
    print(different_words(histogram2))

    """
    WORDS THAT APPEAR IN REDDIT AFTER OSCARS AND NOT BEFORE
    """
    print(subtract(histogram2, histogram1))

    
"""
    # word frequency
    # NLTK - sentiment analysis
"""

if __name__ == "__main__":
    main()