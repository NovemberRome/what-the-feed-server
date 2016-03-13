from django.http import HttpResponse
from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from . import functions
from .models import *
from . import feeds

"""
Gets the Main feed for an user
"""
@csrf_exempt
def getMainFeed(request):
    return functions.invalid_option()


"""
Gets a Subscription's feed
"""
@csrf_exempt
def getFeed(request):
    if request.method != 'POST':
        return functions.invalid_option()
    subsid = request.POST.get('subsid')
    feeds.getCacheForSubs(subsid)
    return functions.invalid_option()


"""
Adds a Subscription
Requires authentication
"""
@csrf_exempt
def addSubscription(request):
    if request.method != 'POST':
        return functions.invalid_option()
    uid = request.POST.get('id')
    password = request.POST.get('password')
    searchParam = request.POST.get('searchparam')
    try:
        sub = UserSubscription(user=User.objects.get(id = uid, password=password), searchParam=searchParam)
        sub.save()
        feeds.addLinksForNewSub(sub)
    except Exception as e:
        print(e)
        return functions.auth_failed()
    return functions.send_response()


"""
Sets/Changes a Subscription
"""
@csrf_exempt
def changeSubscription(request):
    if request.method != 'POST':
        return functions.invalid_option()
    subsId = request.POST.get('subsid')
    pids = request.POST.get('pids')
    if not functions.checkUserCredentials(request):
        functions.auth_failed()
    # auth passed
    curPids = SubscriptionLink.objects.filter(UserSubscription.objects.get(id = subsId))
    # delete can be buggy
    for i in curPids:
        if i.link.id not in pids:
            i.delete()
    return functions.send_response()


"""
Deletes a Subscription
"""
@csrf_exempt
def deleteSubscription(request):
    if request.method != 'POST':
        functions.invalid_option()
    uid = request.POST.get('id')
    password = request.POST.get('password')
    subsid = request.POST.get('subsid')
    user = User.objects.filter(id=uid, password=password)
    if len(user) == 0:
        return functions.auth_failed()
    subs = UserSubscription.objects.filter(id=subsid, user=user[0])
    if len(subs) > 0:
        subs.delete()
        return functions.send_response()
    else:
        return functions.invalid_option()