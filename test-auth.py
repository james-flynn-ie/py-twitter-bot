import tweepy
import os

auth = tweepy.OAuthHandler(os.environ['TWITTER_CONSUMER_API_KEY'], 
    os.environ['TWITTER_CONSUMER_API_SECRET'])
auth.set_access_token(os.environ['TWITTER_ACCESS_TOKEN'], 
    os.environ['TWITTER_ACCESS_TOKEN_SECRET'])

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")