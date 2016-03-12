from django.http import HttpResponse
import json

def invalid_option(msg = 'Invalid Option'):
    data = {
        'status': '404',
        'message': msg
    }
    return HttpResponse(json.dumps(data), content_type='application/json')