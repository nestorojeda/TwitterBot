class Searcher:

    def __init__ (self, terms[],nTweets):
        self.searcherTerms = terms;
        self.nOfTweets = nTweets;

    def start(self, api):
        for term in searcherTerms:
            printer(term);
            for tweet in tweepy.Cursor(api.search, term).items(nOfTweets):
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

    def printer(self, term):
        print("--------------------------\n")
        print("         Searching       ")
        print(term)
        print("\n--------------------------")
