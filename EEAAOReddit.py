import praw
import config
reddit = praw.Reddit(client_id="OhNdbQQX4Lu1YxxL-45Xqg",
                     client_secret="c87ifAS5zYd6QacCuGW2Bwy7GBMEXw",
                     username="SillyYogurt4594",
                     password="ahS25sp+6X&wTQS",
                     user_agent="everything-everywhere")

sub = 'movies'
submissions = reddit.subreddit(sub).top(time_filter="all", limit=5)
top5 = [(submission.title, submission.selftext) for submission in submissions]
print(top5)

