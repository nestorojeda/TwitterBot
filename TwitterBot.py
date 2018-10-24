from time import sleep;
import tweepy;
import Authenticator;
import Searcher;

authO = Authenticator();
authO.authenticate();

searcher = Searcher();

def startBot(searcher, api):
    while True:
        searcher.start(api);
