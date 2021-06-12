from create_api import set_auth, check_env_vars_exist
import os
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
    except Exception:
        print("Authentication failed." +
              "\nCheck that you have set the correct Consumer API " +
              "and Access Token key values.")


if __name__ == "__main__":
    main()
