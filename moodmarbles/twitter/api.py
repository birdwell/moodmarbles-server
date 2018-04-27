import os
import json
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

# Construct the twitter API client
# from os set environment variables
_API = twitter.Api(consumer_key=os.environ[CONSUMER_KEY],
                consumer_secret=os.environ[CONSUMER_SECRET],
                access_token_key=os.environ[ACCESS_TOKEN],
                access_token_secret=os.environ[ACCESS_SECRET])

# Construct the watson NLU unit
_NLU = NLU(version='2018-03-14', username=os.environ[USERNAME], password=os.environ[PASSWORD])

# Get tweets with a certain hashtag
def get_tweets_with_hashtag(hashtag, count):
    # If there is already a file for those tweets,
    # use the cached version
    if os.path.exists('%s.json'%hashtag):
        data = json.load(open('%s.json'%hashtag, 'r'))
        data = data[:count] if len(data) > count else data
        return data
    # Otherwise pull from twitter
    tweets = _API.GetSearch(term=hashtag, include_entities=True, count=count)
    analyses = []
    for tweet in tweets:
        try:
            # Get the sentiment of the tweet
            analysis = get_sentiment(tweet.text)
        except:
            continue
        # Get the maximum emote of the tweet
        max_emote = max(analysis.items(), key=operator.itemgetter(1))
        # Construct the emotion data along with relevant tweet data
        # to better visualize with
        result = {
            'text': tweet.text,
            'tweet': {
                'createdAt': tweet.created_at,
                'favorites': tweet.favorite_count,
                'retweets': tweet.retweet_count,
                'tweetUrl': tweet.urls[0].expanded_url if len(tweet.urls) > 0 else {},
                'profilePic': str(tweet.user.profile_image_url),
                'username': tweet.user.screen_name,
                'profileUrl': str(tweet.user.url),
                'name': tweet.user.name,
                'id': tweet.id_str
            },
            'emotion': max_emote[0],
            'magnitude': max_emote[1]
        }
        analyses.append(result)
    # Return as JSON
    json.dump(analyses, open('%s.json'%hashtag, 'w'))
    return analyses

# Get the sentiment of the tweet using
# the Watson analyzer
def get_sentiment(text):
    response = _NLU.analyze(text=text, features=Features(emotion=EmotionOptions()))
    response = response['emotion']['document']['emotion']
    return response
