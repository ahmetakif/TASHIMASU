import requests

while True:
    r = request.get('http://192.168.1.105')
    print r.status_code
    print r.status_code == requests.codes.ok
    print requests.codes['temporary_redirect']
    print requests.codes.teapot
    print requests.codes['o/']
    print r.text
    print r.json
