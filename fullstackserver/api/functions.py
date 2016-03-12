from django.http import HttpResponse
import json


def auth_failed(code = 302, msg = 'Authentication Problem'):
    return send_response(code, msg)

def invalid_option(code = 404, msg = 'Invalid Option'):
    return send_response(code, msg)

def send_response(code = 200, msg = 'Invalid Option'):
    data = {
        'status': code,
        'message': msg
    }
    return HttpResponse(json.dumps(data), content_type='application/json')