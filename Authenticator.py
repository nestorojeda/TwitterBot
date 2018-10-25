import tweepy
class Authenticator:

    global consumer_key
    global consumer_secret
    global access_token
    global access_token_secret

    def __init__(self):
        f = open("credentials", "r")
        self.consumer_key = f.readline().replace('\n', '')
        self.consumer_secret = f.readline().replace('\n', '')
        self.access_token = f.readline().replace('\n', '')
        self.access_token_secret = f.readline().replace('\n', '')
        f.close()


    def getapi(self):
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)
        api = tweepy.API(auth,  wait_on_rate_limit=True,
                                wait_on_rate_limit_notify=True)
        user = api.me()
        print("Successfully authenticated as: ")
        print(user.name)
        return api