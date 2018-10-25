import tweepy
class Authenticator:

    global consumer_key
    global consumer_secret
    global access_token
    global access_token_secret

    def __init__(self, consumer_key, consumer_secret,
                 access_token, access_token_secret):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token = access_token
        self.access_token_secret = access_token_secret


    def getapi(self):
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)
        api = tweepy.API(auth)
        user = api.me()
        print("Successfully authenticated has: ")
        print(user.name)
        return api