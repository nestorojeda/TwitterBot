from Authenticator import Authenticator
from Searcher import Searcher

authO = Authenticator()
sa = "gofio", "LPAstorm"
searcher = Searcher(sa,500)


while True:
    searcher.start(authO.initGetApiUser())