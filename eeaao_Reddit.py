import praw
from config import client_id, client_secret, username, password, user_agent

"""
config is shared privately on canvas
"""
import emoji
import nltk

nltk.download("stopwords")
from nltk.corpus import stopwords  # ChatGPT

stop_words = set(stopwords.words("english"))

from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download("vader_lexicon")

# in terminal: pip install --user matplotlib
# https://ehmatthes.github.io/pcc/chapter_15/README.html#:~:text=Go%20to%20https%3A%2F%2Fpypi,need%20to%20download%20matplotlib%2D1.4.
import matplotlib.pyplot as plt #https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_features.html


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

    submission = reddit.submission(
        url=URL[0]
    )  # https://praw.readthedocs.io/en/stable/code_overview/models/comment.html
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


def extract_emojis(
    text,
):  # You can use the emoji library. You can check if a single codepoint is an emoji codepoint by checking if it is contained in emoji.UNICODE_EMOJI.
    emojis = []
    unicodeemoji_dict = emoji.get_emoji_unicode_dict(
        "en"
    )  #':man_surfing_medium-light_skin_tone:': '🏄🏼\u200d♂️', ':man_surfing_medium_skin_tone:': '🏄🏽\u200d♂️'...
    unicodeemoji = list(
        unicodeemoji_dict.values()
    )  #'🍽️', '🥠', '⛲', '🖋️', '🕟', '🍀', '🕓', '  🦊', '🖼️', '🍟', '🍤', '🐸', '🐥', '☹️'
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
    text = text.replace(
        chr(8212), " "
    )  # Unicode 8212 is the HTML decimal entity for em dash

    # Remove punctuation
    # text = text.translate(str.maketrans('','', string.punctuation))
    text = text.replace(".", " ")
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
    text = "".join(word_list)

    return text


def process_text(text):
    """
    Makes a sorted histogram dictionary that contains the words from a text with value as the number of times it appears
    """
    hist = {}

    for word in text.split():
        hist[word] = hist.get(word, 0) + 1

    sorted_hist = dict(sorted(hist.items(), key=lambda item: item[1], reverse=True))

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
    Returns the number of different items in a dictionary.
    """
    return len(dictionary)


def print_sentiment_analysis(text):
    score = SentimentIntensityAnalyzer().polarity_scores(text)
    print(score)


def subtract(d1, d2):
    """
    Returns a dictionary with all keys that appear in d1 but not d2.
    """
    res = dict()
    for word in d1:
        if word in d2:
            res[word] = res.get(word, 0)

    return res


def pie_chart(score):
    """
    Prints matplotlab pie chart for vader sentiment analysis
    """
    keys = list(score.keys())
    keys = keys[:3]
    values = list(score.values())
    values = values[:3]

    labels = keys #https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_features.html
    sizes = values
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct="%1.1f%%", colors=["blue", "purple", "red"])
    plt.show()


def main():
    """
    UNCOMMENT BELOW
    """
    # URL1 = [
    #     "https://www.reddit.com/r/flicks/comments/uex2hv/lets_talk_about_everything_everywhere_all_at_once/",
    # ]

    # """
    # Convert to Text
    # """
    # URL1_comments = comments(
    #     URL1
    # )  # comment list before oscars, just comment body, not IDs
    # count_comments(URL1)  # 17 comments
    # URL1_text = "".join(
    #     URL1_comments
    # )  # concatenate all comments into a single string (CHATGPT)
    # print("URL1 Text:", URL1_text)

    # """
    # Pickle Data
    # """
    # import pickle

    # with open(
    #     "eeaao_reviews1.pickle", "wb"
    # ) as f:  # open file in binary mode, write the pickled bytes to the file, ChatGPT
    #     pickle.dump(URL1_text, f)

    # with open("eeaao_reviews1.pickle", "rb") as f:
    #     reloaded_copy_of_URL1text = pickle.load(f)

    # """
    # Extract Emojis: NONE
    # """
    # emojis1 = extract_emojis(reloaded_copy_of_URL1text)
    # print("URL1 Emojis:", emojis1)

    # """
    # Clean Text: remove hyphens, punctuation, emojis, stopwords according to NLTK, make lowercase
    # """
    # clean_text1 = remove_stop_words(reloaded_copy_of_URL1text)
    # print("URL CLeaned Text1: ", clean_text1)

    # """
    # Find Top 50 Words and Frequency
    # """
    # histogram1 = process_text(clean_text1)
    # print_histogram_list(histogram1, 50)

    # """
    # Set of Words: 557 words
    # """
    # print(different_words(histogram1))

    # """
    # Natural Language Processing of the whole of URL1: 
    # {'neg': 0.06, 'neu': 0.719, 'pos': 0.221, 'compound': 0.9999}
    # """
    # print_sentiment_analysis(reloaded_copy_of_URL1text)
    # score1 = {"neg": 0.06, "neu": 0.719, "pos": 0.221, "compound": 0.9999}
    # print(
    #     "The sentimentality score for Reddit Post 1: "
    # ), score1  # text without any cleaning
    # print(pie_chart(score1))

    # URL2 = [
    #     "https://www.reddit.com/r/movies/comments/11pjwko/not_getting_the_hype_for_everything_everywhere/"
    # ]

    # """
    # Convert to Text
    # """
    # URL2_comments = comments(URL2)
    # print(comments(URL2))  # print comment list after oscars, just comment body, not IDs
    # count_comments(URL1)  # 166 comments
    # URL2_text = "".join(
    #     URL2_comments
    # )  # concatenate all comments into a single string (CHATGPT)
    # print("URL Text:", URL2_text)

    # """
    # Pickle Data
    # """
    # import pickle

    # with open("eeaao_reviews2.pickle", "wb") as f:
    #     pickle.dump(URL2_text, f)

    # with open("eeaao_reviews2.pickle", "rb") as f:
    #     reloaded_copy_of_URL2text = pickle.load(f)

    # """
    # Extract Emojis: "URL2 Emojis: ['🤞', '👎', '😭']"
    # """
    # emojis2 = extract_emojis(reloaded_copy_of_URL2text)
    # print("URL2 Emojis:", emojis2)  # no emojis

    # """
    # Clean Text: remove hyphens, punctuation, emojis, stopwords according to NLTK, make lowercase
    # """
    # clean_text2 = remove_stop_words(reloaded_copy_of_URL2text)
    # print("URL CLeaned Text2: ", clean_text2)

    # """
    # Find Top Frequency and Top 50 Words 
    # """
    # histogram2 = process_text(clean_text2)
    # print_histogram_list(histogram2, 50)

    # """
    # Set of Words: 2123 words
    # """
    # print(different_words(histogram2))

    # """
    # Natural Language Processing of the whole of URL2: 
    # {'neg': 0.103, 'neu': 0.68, 'pos': 0.218, 'compound': 1.0}
    # """
    # print_sentiment_analysis(reloaded_copy_of_URL2text)
    # score2 = {"neg": 0.103, "neu": 0.68, "pos": 0.218, "compound": 1.0}
    # print(
    #     "The sentimentality score for Reddit Post 2: "
    # ), score2  # text without any cleaning
    # pie_chart(score2)

    # """
    # WORDS THAT APPEAR IN REDDIT AFTER OSCARS AND NOT BEFORE: 306 Words
    # """
    # after_oscars_uniquewords = subtract(histogram2, histogram1)
    # print(after_oscars_uniquewords)
    # print(different_words(after_oscars_uniquewords))

    # """
    # WORDS THAT APPEAR IN REDDIT BEFORE OSCARS AND NOT AFTER: 306 Words
    # """
    # before_oscars_uniquewords = subtract(histogram1, histogram2)
    # print(before_oscars_uniquewords)
    # print(different_words(before_oscars_uniquewords))


if __name__ == "__main__":
    main()
