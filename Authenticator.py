import tweepy


class Authenticator:
    def __init__(self):
        consumer_key = '' ;
        consumer_secret = ' ';
        access_token = '';
        access_token_secret = ' ';

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret);
        auth.set_access_token(access_token, access_token_secret);
        api = tweepy.API(auth);

    def initGetApiUser(self):
        user = self.api.me();
        print(user.name);
        return self.api;
