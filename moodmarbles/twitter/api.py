import os
import twitter

from moodmarbles.twitter.base import CONSUMER_KEY
from moodmarbles.twitter.base import CONSUMER_SECRET
from moodmarbles.twitter.base import ACCESS_TOKEN
from moodmarbles.twitter.base import ACCESS_SECRET

_API = twitter.Api(consumer_key=os.environ[CONSUMER_KEY],
            	   consumer_secret=os.environ[CONSUMER_SECRET],
            	   access_token_key=os.environ[ACCESS_TOKEN],
            	   access_token_secret=os.environ[ACCESS_SECRET])

def get_tweets_with_hashtag(hashtag, count):
    tweets = _API.GetSearch(term=hashtag, include_entities=True, count=count)
    return [t.text for t in tweets]
