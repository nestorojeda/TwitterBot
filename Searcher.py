import tweepy
from time import sleep;

class Searcher:
    def __init__(self, terms, nTweets):
        self.searcherTerms = terms;
        self.nOfTweets = nTweets;

    def start(self, api):
        for term in self.searcherTerms:
            print("--------------------------\n")
            print("         Searching       ")
            print(term)
            print("\n--------------------------")
            for tweet in tweepy.Cursor(api.search, term).items(self.nOfTweets):
                try:
                    tweet.retweet()
                    tweet.favorite()
                    print('Retweeted the tweet')
                    break
                except tweepy.TweepError as e:
                    print(e.reason)
                except StopIteration:
                    break

        sleep(100);


