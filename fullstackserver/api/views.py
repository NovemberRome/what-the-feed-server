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
            return HttpResponse(json.dumps({'success': 'true'}), content_type='application/json')
            # TODO: return back more data
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
        id = -1
        try:
            user = models.User(username = username, password = password, email=email,
                    firstName = firstName, lastName = lastName)
            user.save()
            id = user.id
            resp = functions.Response()
            resp.add('username', username)
            resp.add('id', id)
            return resp.respond()
        except Exception as e:
            print(e)
            functions.error_happened()
    else:
        return functions.invalid_option()