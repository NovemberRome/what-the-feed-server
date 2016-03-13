"""
Functions to manage feed data and caching
"""

from .models import *
from .integrations import twitter, tumblr, instagram

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