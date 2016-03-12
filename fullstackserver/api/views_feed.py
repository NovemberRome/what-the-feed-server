from django.http import HttpResponse
from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from . import functions
from .models import *

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
    if request.method != 'POST':
        return functions.invalid_option()
    uid = request.POST.get('id')
    password = request.POST.get('password')
    searchParam = request.POST.get('searchparam')
    try:
        sub = UserSubscription(user=User.objects.get(id = uid, password=password), searchParam=searchParam)
        sub.save()
    except Exception as e:
        print(e)
    return functions.invalid_option()


"""
Sets/Changes a Subscription
"""
@csrf_exempt
def changeSubscription(request):
    return functions.invalid_option()