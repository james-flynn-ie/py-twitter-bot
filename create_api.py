import logging
import errno
import os
import sys
import tweepy

logger = logging.getLogger(__name__)
logging.basicConfig(stream=sys.stdout, level=logging.INFO)


def check_env_vars_exist():
    MANDATORY_ENV_VARS = ["TWITTER_CONSUMER_API_KEY",
                          "TWITTER_CONSUMER_API_SECRET",
                          "TWITTER_ACCESS_TOKEN",
                          "TWITTER_ACCESS_TOKEN_SECRET"]

    for env_var in MANDATORY_ENV_VARS:
        if env_var not in os.environ:
            logger.error("{} not found. ".format(env_var) +
                         "Set Twitter App keys as environment variables.")
            sys.exit(errno.EINVAL)


def set_auth(consumer_key, consumer_secret, access_token, access_token_secret):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    return auth


def main():
    check_env_vars_exist()

    auth = set_auth(os.environ['TWITTER_CONSUMER_API_KEY'],
                    os.environ['TWITTER_CONSUMER_API_SECRET'],
                    os.environ['TWITTER_ACCESS_TOKEN'],
                    os.environ['TWITTER_ACCESS_TOKEN_SECRET'])

    api = tweepy.API(auth,
                     wait_on_rate_limit=True,
                     wait_on_rate_limit_notify=True)

    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e

    logger.info("API created")
    return api


if __name__ == '__main__':
    main()
