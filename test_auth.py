from create_api import set_auth, check_env_vars_exist
import errno
import os
import sys
import tweepy


def main():
    check_env_vars_exist()

    auth = set_auth(os.environ['TWITTER_CONSUMER_API_KEY'],
                    os.environ['TWITTER_CONSUMER_API_SECRET'],
                    os.environ['TWITTER_ACCESS_TOKEN'],
                    os.environ['TWITTER_ACCESS_TOKEN_SECRET'])

    api = tweepy.API(auth)

    try:
        api.verify_credentials()
        print("Authentication OK")
    except Exception as e:
        print("Error: {0}".format(e))
        print("\nAuthentication failed." +
              "\nCheck that you have set the correct Consumer API " +
              "and Access Token key values.")
        sys.exit(errno.EACCES)  # Set exit code using errno


if __name__ == "__main__":
    main()
