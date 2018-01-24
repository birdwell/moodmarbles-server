import os
import twitter

API = twitter.Api(consumer_key=os.environ['CONSUMER_KEY'],
	consumer_secret=os.environ['CONSUMER_SECRET'],
	access_token_key=os.environ['ACCESS_TOKEN'],
	access_token_secret=os.environ['ACCESS_SECRET'])

tweets = API.GetSearch(term="%23thunderup",include_entities=True)

for tweet in tweets:
	print ''
	print '--- START OF TWEET ---'
	print tweet.text.strip()
	print 'hashtags: ' + ', '.join(str(hashtag.text) for hashtag in tweet.hashtags) 
	print '--- END OF TWEET ---'
	print ''