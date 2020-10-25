import tweepy
from access_token import ACCESS_TOKENS

tokens = ACCESS_TOKENS

# Authenticate to Twitter
auth = tweepy.OAuthHandler(tokens["CONSUMER_KEY"], tokens["CONSUMER_SECRET"])
auth.set_access_token(tokens["ACCESS_TOKEN"], tokens["ACCESS_TOKEN_SECRET"])

# Create API object
api = tweepy.API(auth)

for tweet in api.search(q="Django", lang="pt", rpp=10):
    print(f"{tweet.user.name}:{tweet.text}\n")