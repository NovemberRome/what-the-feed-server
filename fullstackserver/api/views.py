from django.http import HttpResponse
from django.shortcuts import render
import json

# Create your views here.
def login(request):
    data = {'avi': 'aryan'}
    return HttpResponse(data, content_type='application/json')