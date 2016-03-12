from django.http import HttpResponse
from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from . import functions
from . import models

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
    return functions.invalid_option()


"""
Adds a Subscription
Requires authentication
"""
@csrf_exempt
def addSubscription(request):
    return functions.invalid_option()


"""
Sets/Changes a Subscription
"""
@csrf_exempt
def changeSubscription(request):
    return functions.invalid_option()