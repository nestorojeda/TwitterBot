from Authenticator import Authenticator
from Searcher import Searcher

auth = Authenticator()
api = Authenticator.getapi(auth)
Searcher(api)