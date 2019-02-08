# Twitter bot that retweets using tweepy and heroku.
# Bot also posts news from news paper website.
# Author: Preetam Tamsekar
# Date: Friday, Jan 25 - 2018.

import tweepy
from time import sleep
import time
import schedule
# Import the credentials which consists the Twitter application keys, tokens, and secrets.
# Import the news which consists the code to scrap the latest news from News paper website
 
from credentials import *
import news

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def retweet():
    # q value is the hashtag that you want to retweet
    # item value is the number of retweets you want to tweet with every call of this function
    
    for tweet in tweepy.Cursor(api.search, q='#Nanded OR #नांदेड ').items(10):
        try:
            tweet.retweet()
            print('Tweet by: @' + tweet.user.screen_name)
            print('Retweet published successfully.')

            

        # error handling
        except tweepy.TweepError as error:
            print('\nError. Retweet not successful. Reason: ')
            print(error.reason)

        except StopIteration:
            break

           
def Post_news():
    news = data.News()
    message = "ताजी बातमी : "
    message += news
    try:
        api.update_status(message)
        print('News Posted successfully.')

    except tweepy.TweepError as error:
            print('\nError. News posted failed. Reason: ')
            print(error.reason)



if __name__ == "__main__":
    schedule.every(30).minutes.do(Post_news)
    schedule.every(1).hours.do(retweet)
    while True:
        schedule.run_pending()
        time.sleep(1)