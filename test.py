import requests
import json

login = 'pierrre'
passwd = 'Palyp557'

r = requests.post("https://leekwars.com/api/farmer/login-token", data={'login': login, 'password':passwd})
token = r.json()['token']

#garden_r = requests.post("https://leekwars.com/api/garden/get", data={'token' : token1})

r = requests.get("https://leekwars.com/api/garden/get-solo-challenge/70408", headers={'Content-Type':'application/json', 'Authorization': 'Bearer {}'.format(token)})
print(json.loads(r.content.decode('utf-8')))