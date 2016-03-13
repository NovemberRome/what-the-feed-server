"""
Functions to manage feed data and caching
"""

from .models import *
from .integrations import twitter, tumblr, instagram

def addLinksForNewSub(uSub):
    sp = uSub.searchParam
    # twitter
    links = twitter.getLinks(sp)
    names = twitter.getNames(links)
    count = 0
    for i in range(len(links)):
        if names[i] == 'search':
            continue
        existingLinks = Link.objects.filter(name=names[i], network='twitter')
        if len(existingLinks) > 0:
            link = existingLinks[0]
        else:
            link = Link(url = links[i], network='twitter', name=names[i])
            link.save()
        sl = SubscriptionLink(userSub=uSub, link=link)
        sl.save()
        count+=1
        if count == 3:
            break

    # instagram
    links = instagram.getLinks(sp)
    names = instagram.getNames(links)
    count = 0
    for i in range(len(links)):
        if names[i] == 'search':
            continue
        existingLinks = Link.objects.filter(name=names[i], network='instagram')
        if len(existingLinks) > 0:
            link = existingLinks[0]
        else:
            link = Link(url = links[i], network='instagram', name=names[i])
            link.save()
        sl = SubscriptionLink(userSub=uSub, link=link)
        sl.save()
        count+=1
        if count == 3:
            break