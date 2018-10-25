from Authenticator import Authenticator
from Searcher import Searcher
auth = Authenticator("","","","") #insert your keys here
api = Authenticator.getapi(auth)
searcher = "" #insert yout queries here
Searcher(api, searcher)