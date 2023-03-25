# Text-Analysis-Project
 
1. Project Overview

The three data sources that are referenced and analyzed in this Text Analysis Project are: two reddit posts ("submissions") and the IMDb user reviews relevant to **"Everything Everywhere All at Once"**, the 2022 film that won "Best Picture", "Best Actress", "Best Supporting Actress", "Best Supporting Actor", and "Best Director" during the 2023 Academy Awards. 

The first reddit post is called **"Let's Talk about Everything Everywhere All At Once!"** located under the subreddit "flicks" was posted 11 months ago, approximately in April 2022. (URLs listed in code)

The second reddit post called **"Not Getting the Hype for Everything Everywhere All at Once"** under the subreddit "movies" was posted the day of the Oscars, March 12th. (URLs listed in code)

The techniques that this project focuses on were 
1) finding the top 50 words, and 
1) natural language processing Vader sentimentality score
The sentimentality scores for each reddit posts' comments and the IMDb user reviews summarizes each of medium's sentiment. 

While the movie "Everything Everywhere at Once" received many critic awards, the outcome of the Oscars was **controversal**, whereas public opinion greatly contrasted positive critic reviews as seen by the 7.9/10 IMDb user review score. In this text analysis project, my goal was to better understand the movie's **sentiment through sentiment analysis** on IMDb and use the two separate reddit APIs to see **if sentiment changed drastically before and after the Oscars**. The usage of the top 50 words was to test **what words best captured each source's opinion**.

1. Implementation

A key part of the process for understanding the data also included converting the comments/reviews to plain text, pickling the data, indentifying emojis, cleaning the text (removing NLTK stop words, punctuation, capitalization, emojis, etc.).

**The Sentiment Analysis - Vader Scores + Visualization through Matplotlib.plotpy Pie Chart Design Decision**

After applying vador sentiment analysis on each of the APIs, these were the three APIs obtained:
    Reddit Before Oscars:   {'neg': 0.06, 'neu': 0.719, 'pos': 0.221, 'compound': 0.9999}
    Reddit After Oscars:    {'neg': 0.103, 'neu': 0.68, 'pos': 0.218, 'compound': 1.0}
    IMDb Reviews:           {'neg': 0.094, 'neu': 0.646, 'pos': 0.26, 'compound': 1.0}

Using Matlablib.plotpy, I chose to make the design decision to represent the data using a pie chart with colors coordinating to the negative sentiment and positive sentiment. Negative sentiment is "cold" sentiment, so I chose a cool color such as blue, while the "warm" sentiment is the color red. The neutral sentiment is purple colored, a mix of the blue and red colors.

After applying the pie_chart function to the sentiments that were calculated, based off of this design, you can see whether the blue or red is more dominant. The purple color represents all the filler and stop words that are neutral.

**Bumps in the Road:**
One specific challenge that I faced was when I was importing matplotlib. Even after installing it, I had struggled to import it. For a couple of hours, I was reading on how to re-download it and other ways to implement it. I even asked ChatGPT to help identify the issue. One solution suggested was to download another package on my terminal called "pipdetree" that would be able to tell if there were any conflicting packages. I ran this and it came up with no conflicts with the matplotlab. Ultimately, by uninstalling and reinstalling matplotlab, was I able to fix this problem, but the route to fixing it was quite long and relentless!

**Emojis**
Since there were emojis in the comments of the reddit, I had chosen to extract these emojis when cleaning the data. This was a decision that complicated the process, but I was able to learn how to extract emojis from data!

1. Results

2) **The Sentiment Pie Charts**
The first pie chart represents the sentiment of the first Reddit post (before the Oscars):

The second pie chart represents the sentiment of the second Reddit post (after the Oscars):

The third pie chart respresents the sentiment of the IMDb reviews:

**Conclusions:**
It can be observed that from this small sample of data that there was an increase in the negative sentiment by 4.3% and a decrease in positive sentiment by 0.2%. Therefore, as we assume that the data is representative of the public's opinion (even though the scale is not large enough), there was an increase in negative sentiment while positive sentiment stayed nearly the same. 

The IMDb reviews sentiment best represents the overall public's opinion as this has the largest sample size of reviews. In this, we can see that there is more positive sentiment compared to the Reddit sentiment. While there is positive sentiment, there is still a good amount of negative sentiment at 9.4%. We can conclude from this that the Oscars does not reflect the public's sentiment if the users reviews are accurately representative of the public's opinion.

1) Subtract Function and Words that are Exclusive to each Reddit Post
   
When using the subtraction function to find words that are in each reddit post but not the other post, it was interesting to find that each post has exactly 306 words that are exclusive to their own comments.

CODE from LINES 151-160:
    def subtract(d1, d2):
    """
    Returns a dictionary with all keys that appear in d1 but not d2.
    """
    res = dict()
    for word in d1:
        if word in d2:
            res[word] = res.get(word, 0)

    return res

3) Find Top Frequency and Top 50 Words Function

Finding the top frequency and top 50 words in each dataset was also integral in my project. While finding these top words were not exactly helpful in summarizing the top words that represent the sentiment, it is a useful function for analyzing texts in general, and was important to examine if there was any interesting patterns.

1. Reflection

Challenges:

It was first very difficult to open the comments of the Reddit posts, extract emojis (when the emoji module has been updated and no longer uses the same functions as slack comments recommend), and to fix the relentless error (TypeError: write() argument must be str, not bytes) when pickling the data. By the end of the project, I was able to complete all the analysis in my testing plan which answers my objective in trying to understand the sentiment and if there was a change in sentiment, but there are many ways that I feel that my project can be improved upon.

Improvements:

Many more Reddit posts on the movie exist besides the two that I chose that could help to capture a more complete view of public sentiment. With a larger sample size of comments before the Oscars and comments after the Oscars, a more accurate sentiment analysis can be conducted to represent a more accurate sentiment from the public. 

There may also possibly be comments on the post posted before the Oscars that occurred after the Oscars which skews the controlled variable of my data, the timeframe of comments. It would be more useful to separate comments made before the Oscars and after the Oscars rather than just qualifying the post as created before the Oscars. 

The last largest improvement that I would make to this analysis would be to find access to the IMDb critic reviews and do a sentiment analysis that would compare to the sentiment of the IMDb user reviews. A comparison between the critic and the user review sentiment would also be interesting to examine and make a conclusion about the Oscar's consideration of public input rather than solely critic review. 

Learnings + Future Applications:

Quiz 4 on lists, dictionaries, and tuples really helped me with the skilled needed in this project to transfer between dictionaries and lists. Through this project, I was able apply my learnings on APIs and dictionaries to the reviews and comments on this movie, a real world application. ChatGPT was able to help during moments where I received errors and could not decipher the source of the errors such as when extracting emojis or pickling the data using bytes. 

Initially, the concept of extracting data from APIs was hard for me to grasp. Through this project, I have gained a deeper understanding of APIs and how to extract and manipulate the data from APIs. I know that my skill from this lesson and project will be applied to the future projects that I create in this course and beyond. Utilizing APIs and manipulating data is a concept that all programmers should understand as the internet is an endless source of data that programmers can use as building blocks for all and any types of creative projects.