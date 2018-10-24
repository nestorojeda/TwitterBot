class Authenticator:

    def __init__(self, key, skey,token, stoken):
        self.consumer_key = key;
        self.consumer_secret = skey;
        self.access_token = token;
        self.access_token_secret = stoken;
        self.auth = tweepy.OAuthHandler(consumer_key, consumer_secret);

    def authenticate(self):
        auth.set_access_token(access_token, access_token_secret);

    def initGetApiUser(self):
        api = tweepy.API(auth);
        user = api.me();
        print(user.name);
        return api;
