import create_api
import json
import logging
import sys
import tweepy

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger()

class likeRTListener(tweepy.StreamListener):
    logger.debug("Creating StreamListener")
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        logger.info(f"Processing tweet id {tweet.id}")
        if tweet.in_reply_to_status_id is not None or \
            tweet.user.id == self.me.id:
                # We don't do anything if a tweet is:
                #   - Written by the Twitter account user
                #   - A reply to one of their tweets.
            return

        if not tweet.favorited:
            try:
                tweet.favorite()
            except Exception as e:
                logger.error(f"Failed to Like id# {tweet.id}", exc_info=True)

        if not tweet.retweeted:
            try:
                tweet.retweet()
            except Exception as e:
                logger.error(f"failed to Retweet id# {tweet.id}", exc_info=True)

    def on_error(self, status):
        logger.error(status)

def main(keywords):
    api = create_api.main()
    tweets_listener = likeRTListener(api)
    stream = tweepy.Stream(api.auth, tweets_listener)
    stream.filter(track=keywords, languages=["en"])

if __name__ == "__main__":
    # Each keyword represents an 'OR' condition. 
    # Choose the list carefully as it can get spammy very quickly!
    main(["DevOps", "SRE"])