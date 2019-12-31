import create_api
import logging
import sys
import time
import tweepy

logger = logging.getLogger(__name__)
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

def follow_followers(api):
    logger.info("Retrieving list of followers")

    for follower in tweepy.Cursor(api.followers).items(0):
        logger.debug(f"Checking if {follower.name} is being followed yet")
        if not follower.following:
            logger.info(f"Following {follower.name}")
            follower.follow()
    
    logger.info("Follower list check complete!")

def main():
    api = create_api.main()

    seconds_between_checks = 900

    while True:
        follow_followers(api)
        logger.debug(f"Waiting for {seconds_between_checks} seconds...")
        time.sleep(seconds_between_checks)

if __name__ == "__main__":
    main()