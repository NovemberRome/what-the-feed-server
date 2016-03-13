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

    def __init__(self, link):
        self.name = link.name
        self.link = link

    def getFeeds(self, subsid):
        auth = tweepy.OAuthHandler(AUTH.TWITTER_CONS_KEY, AUTH.TWITTER_CONS_SECRET)
        auth.set_access_token(AUTH.TWITTER_ACC_TOKEN, AUTH.TWITTER_ACC_SECRET)
        api = tweepy.API(auth)
        new_tweets = api.user_timeline(screen_name = self.name, count=10)
        ret = []
        for i in new_tweets:
            # get photo if there
            imageUrl = None
            for media in i.entities.get("media",[{}]):
                # checks if there is any media-entity
                if media.get("type",None) == "photo":
                    # checks if the entity is of the type "photo"
                    imageUrl = media["media_url"]
            # done
            ret.append({
                'subsid': subsid,
                'pid': self.link.pid,
                'network': self.link.network,
                'name': self.name,
                'content': i.text,
                'time': str(i.created_at), # tweepy already takes care of that
                'imageurl': imageUrl,
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
    pass
    # a = TwitterFeed
    # a.getFeeds()
    # links = getLinks('Sachin Tendulkar')
    # names = getNames(links)
    # print(names)
