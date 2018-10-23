from time import sleep
import tweepy

consumer_key = "your key goes here"
consumer_secret = "your key goes here"
access_token = "your key goes here"
access_token_secret = "your key goes here"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

user = api.me()
print(user.name)

searcher = "your queries go here"
numberOfTweets = 100
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
