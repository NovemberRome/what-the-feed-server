"""
Functions to manage feed data and caching
"""
import json
import datetime
from .models import *
from .integrations import twitter, tumblr, instagram


"""
Add Links for New subscription made
Use existing links if possible
"""
def addLinksForNewSub(uSub):
    getLinksForNetwork(uSub, twitter, 'twitter')
    getLinksForNetwork(uSub, instagram, 'instagram')
    getLinksForNetwork(uSub, tumblr, 'tumblr')


def getLinksForNetwork(uSub, networkClass, networkStr):
    sp = uSub.searchParam
    links = networkClass.getLinks(sp)
    names = networkClass.getNames(links)
    count = 0
    for i in range(len(links)):
        if names[i] == 'search':
            continue
        existingLinks = Link.objects.filter(name=names[i], network=networkStr)
        if len(existingLinks) > 0:
            link = existingLinks[0]
        else:
            link = Link(url = links[i], network=networkStr, name=names[i])
            link.save()
        sl = SubscriptionLink(userSub=uSub, link=link)
        sl.save()
        count+=1
        if count == 2:
            break


"""
Gets feed for user
"""
def getCacheForUser(user):
    usubs = UserSubscription.objects.filter(user=user)
    feed = []
    for i in usubs:
        feed += getCacheForSubs(i.id)
    return feed

"""
Makes cache for a subscription if needed
returns it
"""
def getCacheForSubs(subsid):
    uSub = UserSubscription.objects.get(id=subsid)
    subLinks = SubscriptionLink.objects.filter(userSub=uSub)
    feedData = []
    for i in subLinks:
        if i.link.network == 'twitter':
            feedData += getCacheForNetwork(i.link, twitter.TwitterFeed)
        elif i.link.network == 'instagram':
            feedData += getCacheForNetwork(i.link, instagram.InstagramFeed)
        elif i.link.network == 'tumblr':
            feedData += getCacheForNetwork(i.link, tumblr.TumblrFeed)
        else:
            pass
    return feedData

# TODO: refresh cache by time
def getCacheForNetwork(link, networkClass):
    curCaches = Cache.objects.filter(link=link)
    if len(curCaches) > 0:
        data = curCaches[0].data
        datalist = json.loads(data)
    else:
        f = networkClass(link.name)
        datalist = f.getFeeds()[:]
        data = json.dumps(datalist)
        cache = Cache(data=data, link=link, expiry=str(datetime.datetime.now()))
        cache.save()
    return datalist