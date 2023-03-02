# !pip install tweepy
import sys
import tweepy
import pandas as pd
from datetime import datetime

# Authenticate to Twitter
# This is Reza's API Key, please don't share the key.
# Or you can create your own key on Twitter Developer

# api key
api_key = '5ziWfVLWY4QygWCy3AzD2UQbQ'
# api secret key
api_secret_key = 'bLdFyVDeDiiGzJaMYwlHwq5LAIbeS3J53Z1gK2ITCRTZVnbHMR'
# access token
access_token = '115651874-xWpSpguXOlah1PtpcmXC7VjWAcryLxnGG1MxF141'
# access token secret
access_token_secret = 'U3Ie5qhDa3f5DbFikPgor3xL7o3SHjhVwqdl2haSPYuv7'


authentication = tweepy.OAuthHandler(api_key, api_secret_key)
authentication.set_access_token(access_token, access_token_secret)
api = tweepy.API(authentication, wait_on_rate_limit=True)

# Define the search term and the date_since date as variables [CHANGE THIS!]
topics = 'safe-t'
keywords = ['purge+law','safe-t', 'Pretrial Fairness Act']

def scrape_t(keywords): # changed the function name to scrape_t
    '''Scrape tweets from Twitter using keywords
    Input: keywords (list)
    Output: csv file
    '''
    max_tweets = 1000
    column_list = [
    'created_at',
    'id_str',
    'source',
    'text',
    'in_reply_to_status_id_str',
    'user.id_str',
    'user.created_at',
    'user.name',
    'user.screen_name',
    'user.description',
    'user.location',
    'user.verified',
    'user.followers_count',
    'user.friends_count',
    'user.statuses_count',
    'user.listed_count',
    'user.favourites_count',
    'retweet_count',
    'favorite_count',
    'favorited',
    'retweeted',
    'lang',
    'coordinates',
    'keyword'
    ]
    tweets_df = pd.DataFrame(columns=column_list)
    for text in keywords:
        # Creation of query method using parameters
        tweets = tweepy.Cursor(api.search_tweets,q=text +'-filter:retweets', count=100).items(max_tweets) #until='2023-01-26'

        # Pulling information from tweets iterable object
        # Add or remove tweet information you want in the below list comprehension
        tweets_list = [[tweet.created_at,
                        tweet.id_str,
                        tweet.source,
                        tweet.text,
                        tweet.in_reply_to_status_id_str,
                        tweet.user.id_str,
                        tweet.user.created_at,
                        tweet.user.name,
                        tweet.user.screen_name,
                        tweet.user.description,
                        tweet.user.location,
                        tweet.user.verified,
                        tweet.user.followers_count,
                        tweet.user.friends_count,
                        tweet.user.statuses_count,
                        tweet.user.listed_count,
                        tweet.user.favourites_count,
                        tweet.retweet_count,
                        tweet.favorite_count,
                        tweet.favorited,
                        tweet.retweeted,
                        tweet.lang,
                        tweet.coordinates,
                        text
                        ] for tweet in tweets]

        # Creation of dataframe from tweets_list
        # Did not include column names to simplify code
        tweets_df = pd.concat([tweets_df, (pd.DataFrame(tweets_list, columns = column_list))])
        #tweets_df = tweets_df.append(pd.DataFrame(tweets_list, columns = column_list), ignore_index = True)

        print(text+' done\n')

        # Saving dataframe as a CSV file
        file_name = 'tweets_'+topics+datetime.now().strftime('%Y%m%d_%H')+'.csv'
        tweets_df.to_csv(file_name, index=False)
        print('File saved as '+file_name)

    return None

if __name__ == "__main__":
    scrape_t(keywords)