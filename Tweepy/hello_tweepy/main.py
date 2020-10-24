import tweepy

auth = tweepy.OAuthHandler("asda", "asdas")
auth.set_access_token("asda-asda", "asda")

api = tweepy.API(auth)

api.update_status("Hello friend, this is a bot")