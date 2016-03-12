from django.http import HttpResponse
from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from . import functions

def login(request):
    data = {'avi': 'aryan'}
    return HttpResponse(data, content_type='application/json')


@csrf_exempt
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        email = request.POST.get('email', '')
        firstName = request.POST.get('firstname', '')
        lastName = request.POST.get('lastname', '')
        #render(request, 'simpleview.html', {username : 'value'})
        return HttpResponse(json.dumps({'username': username}), content_type='application/json')
    else:
        return functions.invalid_option()