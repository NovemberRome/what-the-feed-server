import requests

url = 'http://localhost/api/'

def register():
    r = requests.post(url + 'register', data = {'username': 'aviaryan', 'password': 'something', 'email': 'avi@aryan.com'})
    print(r.content)

def login():
    r = requests.post(url + 'login', data = {'username': 'aviaryan', 'password': 'something'})
    print(r.content)

if __name__ == '__main__':
    register()
    login()