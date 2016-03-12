import tweepy
from auth import AUTH
# from .auth import AUTH
# TODO: Fix tweet with image

class TwitterFeed():

    name = 'username'

    def __init__(self, username):
        self.name = username

    def getFeeds(self):
        auth = tweepy.OAuthHandler(AUTH.TWITTER_CONS_KEY, AUTH.TWITTER_CONS_SECRET)
        auth.set_access_token(AUTH.TWITTER_ACC_TOKEN, AUTH.TWITTER_ACC_SECRET)
        api = tweepy.API(auth)
        new_tweets = api.user_timeline(screen_name = self.name, count=20)
        ret = []
        for i in new_tweets:
            ret.append({
                'text': i.text,
                'time': i.created_at,
                'imageUrl': None,
                'url': 'https://twitter.com/statuses/' + i.id_str
            })
        return ret

if __name__ == '__main__':
    a = TwitterFeed('aviaryan123')
    a.getFeeds()