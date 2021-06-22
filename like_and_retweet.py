import create_api
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
        logger.info(f"Liking and RTing id# {tweet.id}")
        if tweet.in_reply_to_status_id is not None or \
           tweet.user.id == self.me.id:
            # We don't do anything if a tweet is either:
            #   - Written by the Twitter account user.
            #   - A reply to one of the Twitter account user's tweets.
            return

        if not tweet.favorited:
            try:
                tweet.favorite()
            except Exception:
                logger.exception(f"Failed to Like id# {tweet.id}",
                                 exc_info=True)

        if not tweet.retweeted:
            try:
                tweet.retweet()
            except Exception:
                logger.exception(f"Failed to Retweet id# {tweet.id}",
                                 exc_info=True)

    def on_error(self, status):
        logger.error(status)


def main(keywords):
    api = create_api.main()
    tweets_listener = likeRTListener(api)
    stream = tweepy.Stream(api.auth, tweets_listener)

    logger.info(f"Filtering by keywords {keywords}")
    stream.filter(track=keywords, languages=["en"])


if __name__ == "__main__":
    # Each keyword represents an 'OR' condition.
    # Choose the list carefully as it can get spammy very quickly!
    main(["DevOps", "SRE"])
