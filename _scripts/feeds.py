import requests

url = 'http://10.100.2.81:5123/api/feed/'

def addsubs():
    r = requests.post(url + 'addsubscription', data = {'id': 1, 'password': 'something', 'searchparam': 'Batman vs Superman'})
    print(r.content)

def delsubs():
    r = requests.post(url + 'deletesubscription', data = {'id': 1, 'password': 'something', 'subsid': 2})
    print(r.content)

def login():
    r = requests.post(url + 'login', data = {'username': 'aviaryan', 'password': 'something'})
    print(r.content)

if __name__ == '__main__':
    addsubs()
    #delsubs()
    #login()