# py-twitter-bot

Twitter bot which uses [Tweepy](https://github.com/tweepy/Tweepy), a Twitter API Wrapper written in Python.

The bot automatically follows new followers.

## Configuration

### Create A Twitter App

* **Create a Twitter Developer's Account:** [https://developer.twitter.com/en/apply-for-access](https://developer.twitter.com/en/apply-for-access)
* **Create an App in your Twitter Developer's account.** You can leave most of the fields blank, but you must complete the following mandatory fields:
  * _App Name_: This name will appear when the app tweets on your behalf.
  * _Application Description_: A short description about what the app does.
  * _Website URL_: The URL will be referenced by the app when posting, so any personal website will do.
  * _Tell us how this app will be used_: This is used by Twitter staff to see if you will follow their [restricted usage policies](https://developer.twitter.com/en/developer-terms/more-on-restricted-use-cases). I stated that the app was an 'Application for automatically following users who follow me.'
* **Generate an access token and secret for the App.** Make a note of the token and secret values, along with the consumer API and secret keys, as they are used when configuring the runtime environment.

### Clone the py-twitter-bot Git repository

* **[git clone](https://git-scm.com/docs/git-clone) the [py-twitter-bot](https://github.com/james-flynn-ie/py-twitter-bot) repository.**

### Set Up Python Environment

* **[Install Python 3](https://www.python.org/downloads/), if not already installed.**
* **[Install pip](https://pip.pypa.io/en/stable/installing/#installing-with-get-pip-py), if not already installed.**
* **[Install Virtualenv](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/).**
* **Change to the directory containing the cloned py-twitter-bot repository, and [create a virtual environment](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment).**
* **Prior to running any Python commands in the directory, [run the virtualenv activate script to launch the virtual environment](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/#activating-a-virtual-environment).**

### Configure Runtime Environment

* **Set the following environment variables using the values taken from the Twitter App:**
  * TWITTER_ACCESS_TOKEN
  * TWITTER_ACCESS_TOKEN_SECRET
  * TWITTER_CONSUMER_API_KEY
  * TWITTER_CONSUMER_API_SECRET

* **Run the following command in the cloned directory:** This will install the Python dependencies required by py-twitter-bot:

```bash
   pip install -r requirements.txt
```

* **Verify that the environment is configured correctly** by executing the [test_auth.py](https://github.com/james-flynn-ie/py-twitter-bot/blob/master/test_auth.py) script from the CLI:

```bash
    python ./test_auth.py
```

If you see the message, "Authentication OK" then you are all set!

## Run Application

### follow_all_followers.py

#### Description

follow_all_followers checks if you are already following all of the Twitter users who are your followers. Once the script has checked your entire list of followers, then it waits 15 minutes and then checks again.

#### Usage

```bash
python follow_all_followers.py
```

### like_and_retweet.py

#### Description

like_and_retweet performas a search for keywords specified in like_and_retweet:main(). It then likes and retweets everything returned as search results.

**Caution**: The number of likes and retweets can be quite large and spammy if the keywords are too vague. Please consider improving the list with more specific keywords before running!

```python
main(["DevOps", "SRE"])
```

#### Usage

```bash
python like_and_retweet.py
```
