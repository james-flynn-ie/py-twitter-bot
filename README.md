# py-twitter-bot

Twitter bot which uses [Tweepy](https://github.com/tweepy/Tweepy), a Twitter API Wrapper written in Python.

The bot automatically follows new followers.

## Configuration

* **Create a Twitter Developer's Account:** [https://developer.twitter.com/en/apply-for-access](https://developer.twitter.com/en/apply-for-access)
* **Create an App in your Twitter Developer's account.**
* **Generate an access token and secret for the App.** Make a note of the token and secret values, along with the consumer API and secret keys, as they are used in the next step.
* **Set the following environment variables using the values taken from the Twitter App:**
  * TWITTER_ACCESS_TOKEN
  * TWITTER_ACCESS_TOKEN_SECRET
  * TWITTER_CONSUMER_API_KEY
  * TWITTER_CONSUMER_API_SECRET
* **Verify that these environment variables are set correctly** by executing the [test-auth.py](https://github.com/james-flynn-ie/py-twitter-bot/blob/master/test-auth.py) script from the CLI:

```bash
    python ./test-auth.py
```
