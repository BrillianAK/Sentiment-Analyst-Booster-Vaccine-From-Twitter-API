# from tkinter.tix import TCL_WINDOW_EVENTS, Tree
from unicodedata import name
from numpy import place
import tweepy
import pandas as pd
from time import time

start = time()
client = tweepy.Client(bearer_token="AAAAAAAAAAAAAAAAAAAAAFsnZAEAAAAA2G4zTh3dQ1o6cu4FOZ874giDGJs%3DwUBYGxuH1oPOBQnRKwiQ53JX4QVvDuxHJ9o4elyqoAu5pNuUbL")

query = "vaksin booster"
# query = "booster -is:retweet"
# query = "booster -has:media"

# response = client.search_recent_tweets(query=query, max_results = 10, tweet_fields=['created_at','lang'])

# for tweet in response.data:
    # print(tweet.text)
    # print(tweet.created_at)
    # print(tweet.lang)

text = []
tanggal = []
lang = []


for tweet in tweepy.Paginator(client.search_recent_tweets, query=query, max_results=100, tweet_fields=['created_at','lang'],expansions=["geo.place_id"]).flatten(limit=3000):
    # print(tweet.text)
    if tweet.text:
        if tweet.created_at:
            if tweet.lang:
                text.append(tweet.text)
                tanggal.append(tweet.created_at)
                lang.append(tweet.lang)

df = pd.DataFrame(text, columns=['text']) 
df['tanggal'] = tanggal
df['bahasa'] = lang
df = df.drop_duplicates(subset=['text'])
# print(df.head(10))

file_name = "twitter_lebaran.csv"

df.to_csv(file_name)
# print('Time taken to run: {0:.19f} seconds\n'.format(time() - start))