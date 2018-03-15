import os
import twitter
import operator

from moodmarbles.twitter.base import CONSUMER_KEY
from moodmarbles.twitter.base import CONSUMER_SECRET
from moodmarbles.twitter.base import ACCESS_TOKEN
from moodmarbles.twitter.base import ACCESS_SECRET
from moodmarbles.twitter.base import USERNAME
from moodmarbles.twitter.base import PASSWORD

from watson_developer_cloud import NaturalLanguageUnderstandingV1 as NLU
from watson_developer_cloud.natural_language_understanding_v1 import Features
from watson_developer_cloud.natural_language_understanding_v1 import EmotionOptions

_API = twitter.Api(consumer_key=os.environ[CONSUMER_KEY],
            	   consumer_secret=os.environ[CONSUMER_SECRET],
            	   access_token_key=os.environ[ACCESS_TOKEN],
            	   access_token_secret=os.environ[ACCESS_SECRET])

_NLU = NLU(version='2018-03-14', username=os.environ[USERNAME], password=os.environ[PASSWORD])

def get_tweets_with_hashtag(hashtag, count):
    tweets = _API.GetSearch(term=hashtag, include_entities=True, count=count)
    analyses = []
    for tweet in tweets:
        analysis = get_sentiment(tweet.text)
        max_emote = max(analysis.items(), key=operator.itemgetter(1))[0]
        result = {'text': tweet.text,
        		  'emotion': max_emote}
        analyses.append(result)
    return analyses

def get_sentiment(text):
	response = _NLU.analyze(text=text, features=Features(emotion=EmotionOptions()))
	response = response['emotion']['document']['emotion']
	return response
