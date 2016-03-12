from django.http import HttpResponse
from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from . import functions
from . import models


"""
Login a user
"""
@csrf_exempt
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = models.User.objects.filter(username=username, password=password)
        if len(user) == 1:
            resp = functions.Response()
            resp.add('subscriptions', [])
            return resp.respond()
        else:
            return functions.auth_failed()
    else:
        return functions.invalid_option()


"""
Registers a user
"""
@csrf_exempt
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username') # None default if no second param
        password = request.POST.get('password')
        email = request.POST.get('email')
        firstName = request.POST.get('firstname')
        lastName = request.POST.get('lastname')
        try:
            user = models.User(username = username, password = password, email=email,
                    firstName = firstName, lastName = lastName)
            user.save()
            uid = user.id
            resp = functions.Response()
            resp.add('username', username)
            resp.add('id', uid)
            return resp.respond()
        except Exception as e:
            print(e)
            return functions.error_happened()
    else:
        return functions.invalid_option()