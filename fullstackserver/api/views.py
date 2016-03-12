from django.http import HttpResponse
from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from . import functions
from . import models

def login(request):
    data = {'avi': 'aryan'}
    return HttpResponse(data, content_type='application/json')


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
        except Exception as e:
            print(e)
        return HttpResponse(json.dumps({'username': username, 'id': id}), content_type='application/json')
    else:
        return functions.invalid_option()