from time import sleep
import tweepy

class Searcher:
    def __init__(self,api, searcher,):
        numberOfTweets = 500
        while True:
            for search in searcher:
                print("--------------------------\n")
                print("         Searching       ")
                print(search)
                print("\n--------------------------")
                for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
                    try:
                        tweet.retweet()
                        tweet.favorite()
                        print('Retweeted the tweet')
                        break
                    except tweepy.TweepError as e:
                        print(e.reason)
                    except StopIteration:
                        break
                sleep(100)