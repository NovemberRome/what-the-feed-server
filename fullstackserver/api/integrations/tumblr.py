# register for app on tumblr, get the key, use the api
# http://stackoverflow.com/questions/14514522/how-to-extract-data-from-tumblr-api-json
# use cons key
# http://api.tumblr.com/v2/blog/myblog.tumblr.com/info?api_key=hjvdX6OC5x958s4S2AqQEdNo8w2DmWFWHBDNXXyJ26ru5bnYFd

import requests
from auth import AUTH
import json
# from .auth import AUTH

class TumblrFeed:

    name = 'aviaryan'

    def __init__(self, name):
        self.name = name + '.tumblr.com'

    def getFeeds(self):
        url = 'https://api.tumblr.com/v2/blog/' + self.name + '/posts/text?' + \
              'api_key=' + AUTH.TUMBLR_CONS_KEY + '&limit=10' + '&notes_info=False' + '&filter=text' + \
            '&type=text'
        print(url)
        r = requests.get(url)
        obj = json.loads(r.content.decode(encoding='utf-8'))
        posts = obj['response']['posts']
        ret = []
        for i in posts:
            ret.append({
                'text': i['body'],
                'time': i['date'],
                'imageUrl': None,
                'url': i['post_url']
            })
        return ret


if __name__=='__main__':
    x = TumblrFeed('aviaryan')
    x.getFeeds()
