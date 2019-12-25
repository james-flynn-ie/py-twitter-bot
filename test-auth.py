import os
import tweepy

def check_env_vars_exist():
  MANDATORY_ENV_VARS = ["TWITTER_CONSUMER_API_KEY", "TWITTER_CONSUMER_API_SECRET", "TWITTER_ACCESS_TOKEN", "TWITTER_ACCESS_TOKEN_SECRET"]
  
  for env_var in MANDATORY_ENV_VARS:
    if env_var not in os.environ:
      raise EnvironmentError("{} not found. Twitter App keys must be set as environment variables.".format(env_var))

def main():
  check_env_vars_exist()
  
  auth = tweepy.OAuthHandler(os.environ['TWITTER_CONSUMER_API_KEY'], 
      os.environ['TWITTER_CONSUMER_API_SECRET'])
  auth.set_access_token(os.environ['TWITTER_ACCESS_TOKEN'], 
      os.environ['TWITTER_ACCESS_TOKEN_SECRET'])
  
  api = tweepy.API(auth)
  
  try:
      api.verify_credentials()
      print("Authentication OK")
  except:
      print("Error during authentication")

if __name__== "__main__":
  main()
