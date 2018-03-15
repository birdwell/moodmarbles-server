import logging

from moodmarbles.base.app import get_app

from moodmarbles.views.views import TWITTER

logging.basicConfig(level = logging.DEBUG)
logger = logging.getLogger(__name__)

if __name__ == '__main__':
    app = get_app()
    app.register_blueprint(TWITTER, url_prefix="/twitter")
    logging.info(app.url_map)
    app.run(threaded=True, debug=True, port=5001)
