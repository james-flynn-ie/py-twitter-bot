import create_api
import logging
import sys
import time
import tweepy

logger = logging.getLogger(__name__)
logging.basicConfig(stream=sys.stdout, level=logging.INFO)

def follow_followers(api):
    logger.info("Retrieving list of followers.")

    try:
        for follower in tweepy.Cursor(api.followers).items():
            logger.debug(f"Checking if {follower.name} is being followed yet")
            if not follower.following:
                logger.info(f"Following {follower.name}")
                follower.follow()
    except Exception as e:
        logger.error(f"Failed to follow {follower.name}", exc_info=True)
        raise e

    logger.info("Finished checking follower list!")

def main():
    seconds_between_checks = 900

    api = create_api.main()
    
    while True:
        follow_followers(api)
        logger.debug(f"Waiting for {seconds_between_checks} seconds.")
        time.sleep(seconds_between_checks)

if __name__ == "__main__":
    main()