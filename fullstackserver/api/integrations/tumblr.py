# register for app on tumblr, get the key, use the api
# http://stackoverflow.com/questions/14514522/how-to-extract-data-from-tumblr-api-json
# use cons key
# http://api.tumblr.com/v2/blog/myblog.tumblr.com/info?api_key=hjvdX6OC5x958s4S2AqQEdNo8w2DmWFWHBDNXXyJ26ru5bnYFd

import requests
import json
import re
try:
    from .auth import AUTH
    from .utils import *
    from .googlesearch import *
except SystemError:
    from auth import AUTH
    from utils import *
    from googlesearch import *

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
                'text': i['body'][:200],
                'time': timeToStr(i['date']),
                'imageurl': None,
                'url': i['post_url']
            })
        return ret

def getLinks(searchterm):
    links = googleSearchLinks(searchterm + ' - Tumblr', r'http.*?\/\/[^\/]*?tumblr\.com\/?$')
    return links

def getNames(links):
    names = []
    for i in links:
        names.append(getName(i))
    return names

def getName(link):
    name = re.sub(r'http.*\/\/', '', link)
    name = re.sub(r'\.tumblr.*', '', name)
    return name

if __name__=='__main__':
    # x = TumblrFeed('aviaryan')
    # x.getFeeds()
    links = getLinks('FC Barcelona')
    names = getNames(links)
    print(names)
