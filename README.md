# py-twitter-bot

Twitter bot which uses [Tweepy](https://github.com/tweepy/Tweepy), a Twitter API Wrapper written in Python.

The bot automatically follows new followers.

## Configuration

### Create Twitter App

* **Create a Twitter Developer's Account:** [https://developer.twitter.com/en/apply-for-access](https://developer.twitter.com/en/apply-for-access)
* **Create an App in your Twitter Developer's account.** You can leave most of the fields blank, but you must complete the following mandatory fields:
  * _App Name_: This name will appear when the app tweets on your behalf.
  * _Application Description_: A short description about what the app does.
  * _Website URL_: The URL will be referenced by the app when posting, so any personal website will do.
  * _Tell us how this app will be used_: This is used by Twitter staff to see if you will follow their [restricted usage policies](https://developer.twitter.com/en/developer-terms/more-on-restricted-use-cases). I stated that the app was an 'Application for automatically following users who follow me.'
* **Generate an access token and secret for the App.** Make a note of the token and secret values, along with the consumer API and secret keys, as they are used in the next step.

### Set Up Python Environment

* **[Install Python 3](https://www.python.org/downloads/), if not already installed.**
* **[Install pip](https://pip.pypa.io/en/stable/installing/#installing-with-get-pip-py), if not already installed.** 
* **[Install Virtualenv](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/).**
* **Change to the cloned directory, and [create a virtual environment](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment).**
* **Prior to running any Python commands in the directory, [run the virtualenv activate script to launch the virtual environment](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/#activating-a-virtual-environment).**

### Configure Runtime Environment

* **Set the following environment variables using the values taken from the Twitter App:**
  * TWITTER_ACCESS_TOKEN
  * TWITTER_ACCESS_TOKEN_SECRET
  * TWITTER_CONSUMER_API_KEY
  * TWITTER_CONSUMER_API_SECRET
* **Verify that these environment variables are set correctly** by executing the [test-auth.py](https://github.com/james-flynn-ie/py-twitter-bot/blob/master/test-auth.py) script from the CLI:

```bash
    python ./test-auth.py
```
