import tweepy
from .access_token import ACCESS_TOKENS

tokens = ACCESS_TOKENS

# Authenticate to Twitter
auth = tweepy.OAuthHandler(tokens["CONSUMER_KEY"], tokens["CONSUMER_SECRET"])
auth.set_access_token(tokens["ACCESS_TOKEN"], tokens["ACCESS_TOKEN_SECRET"])

# Create API object
api = tweepy.API(auth)

# Create a tweet
api.update_status("Hello friend, this is a bot")
