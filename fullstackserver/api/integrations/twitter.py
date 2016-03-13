import tweepy
import re

try:
    from .auth import AUTH
    from .utils import *
    from .googlesearch import *
except SystemError:
    from auth import AUTH
    from utils import *
    from googlesearch import *
# TODO: Fix tweet with image

class TwitterFeed:

    name = 'aviaryan123'

    def __init__(self, username):
        self.name = username

    def getFeeds(self):
        auth = tweepy.OAuthHandler(AUTH.TWITTER_CONS_KEY, AUTH.TWITTER_CONS_SECRET)
        auth.set_access_token(AUTH.TWITTER_ACC_TOKEN, AUTH.TWITTER_ACC_SECRET)
        api = tweepy.API(auth)
        new_tweets = api.user_timeline(screen_name = self.name, count=10)
        ret = []
        for i in new_tweets:
            ret.append({
                'name': self.name,
                'content': i.text,
                'time': str(i.created_at), # tweepy already takes care of that
                'imageurl': None,
                'url': 'https://twitter.com/statuses/' + i.id_str
            })
        return ret

def getLinks(searchterm):
    links = googleSearchLinks(searchterm + ' - Twitter', r'http.*?\/\/[^\/]*?twitter\.com\/[^\/]+\/?$')
    print(links)
    return links

def getNames(links):
    names = []
    for i in links:
        names.append(getName(i))
    return names

def getName(link):
    name = re.sub(r'.*twitter.com\/', '', link)
    name = name.replace('/', '')
    return name

if __name__ == '__main__':
    # a = TwitterFeed('aviaryan123')
    # a.getFeeds()
    links = getLinks('Sachin Tendulkar')
    names = getNames(links)
    print(names)
