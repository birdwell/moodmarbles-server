import os
import json

from flask import jsonify
from flask import request
from flask import Blueprint

from moodmarbles.base.app import get_app

from moodmarbles.twitter.api import get_tweets_with_hashtag

APP = get_app()

POST = 'POST'
GET = 'GET'

TWITTER = Blueprint("twitter", __name__)

@TWITTER.route('/tweets', methods=[GET])
def tweets():
    hashtag = request.args.get("hashtag")
    count = request.args.get("count")
    count = 15 if not count else count
    texts = get_tweets_with_hashtag(hashtag=hashtag, count=count)
    return jsonify(texts), 200

@TWITTER.route('/cached', methods=[GET])
def cached():
    files = os.listdir('./')
    json_files = [f.split('.')[0] for f in files if f.endswith('.json')]
    return jsonify(json_files), 200

