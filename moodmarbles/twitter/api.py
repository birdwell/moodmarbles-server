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

_API = twitter.Api(consumer_key=os.environ[CONSUMER_KEY],
                consumer_secret=os.environ[CONSUMER_SECRET],
                access_token_key=os.environ[ACCESS_TOKEN],
                access_token_secret=os.environ[ACCESS_SECRET])

_NLU = NLU(version='2018-03-14', username=os.environ[USERNAME], password=os.environ[PASSWORD])

def get_tweets_with_hashtag(hashtag, count):
    if os.path.exists('%s.json'%hashtag):
        data = json.load(open('%s.json'%hashtag, 'r'))
        data = data[:count] if len(data) > count else data
        return data
    tweets = _API.GetSearch(term=hashtag, include_entities=True, count=count)
    analyses = []
    for tweet in tweets:
        try:
            analysis = get_sentiment(tweet.text)
        except:
            continue
        max_emote = max(analysis.items(), key=operator.itemgetter(1))
        result = {
            'text': tweet.text,
            'tweet': {
                'createdAt': tweet.created_at,
                'favorites': tweet.favorite_count,
                'retweets': tweet.retweet_count,
                'tweetUrl': tweet.urls[0].expanded_url if len(tweet.urls) > 0 else {},
                'profilePic': str(tweet.user.profile_image_url),
                'username': tweet.user.screen_name,
                'profileUrl': str(tweet.user.url)
            },
            'emotion': max_emote[0],
            'magnitude': max_emote[1]
        }
        analyses.append(result)
    json.dump(analyses, open('%s.json'%hashtag, 'w'))
    return analyses

def get_sentiment(text):
    response = _NLU.analyze(text=text, features=Features(emotion=EmotionOptions()))
    response = response['emotion']['document']['emotion']
    return response
