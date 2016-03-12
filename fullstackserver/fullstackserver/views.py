from django.http import HttpResponse
from django.shortcuts import render
from django.core import serializers
import json

def test_view(request):
    data = {'avi': 'aryan', 'pratyush': 'singh'}
    return HttpResponse(data, content_type='application/json')
    #return render(request, 'simpleview.html', {'data': 'awesome'})