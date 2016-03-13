import requests

url = 'http://10.100.2.81:5123/api/feed/'
#url = 'http://whatthefeed.herokuapp.com/api/feed/'

def addsubs():
    r = requests.post(url + 'addsubscription', data = {'id': 2, 'password': 'a', 'searchparam': 'Artificial Intelligence'})
    print(r.content)

def delsubs():
    r = requests.post(url + 'deletesubscription', data = {'id': 1, 'password': 'something', 'subsid': 2})
    print(r.content)

def getfeed():
    r = requests.post(url + 'getfeed', data = {'id': 1, 'password': 'something', 'subsid': 1})
    print(r.content)

def getmainfeed():
    r = requests.post(url + 'getmainfeed', data = {'id': 1, 'password': 'something', 'subsid': 1})
    print(r.content)

if __name__ == '__main__':
    addsubs()
    #delsubs()
    #getfeed()
    #getmainfeed()