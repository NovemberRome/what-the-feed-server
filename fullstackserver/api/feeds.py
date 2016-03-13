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
        if count == 3:
            break

"""
Makes cache for a subscription if needed
returns it
"""
def getCacheForSubs(subsid):
    uSub = UserSubscription.objects.get(id=subsid)
    subLinks = SubscriptionLink.objects.filter(userSub=uSub)
    for i in subLinks:
        if i.link.network == 'twitter':
            f = twitter.TwitterFeed(i.link.name)
            data = json.dumps(f.getFeeds())
            Cache.objects.filter(link=i.link).delete() # delete old
            cache = Cache(data=data, link=i.link, expiry=str(datetime.datetime.now()))
            cache.save()
    return