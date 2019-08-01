import requests
from random import randint

login = 'pierrre'
passwd = 'Palyp557'
nb_combat = 100
bout_vert = 57610


# connexion
r = requests.post("https://leekwars.com/api/farmer/login-token", data={'login': login, 'password':passwd})
token = r.json()['token']
header = {'Content-Type': 'application/json', 'Authorization': 'Bearer {}'.format(token), "Cookie": "PHPSESSID="+ str(randint(0, 1000))};

for x in range(0, 2):
    r = requests.get("https://leekwars.com/api/garden/get-leek-opponents/" + str(bout_vert), headers=header)
    print(header)
    vilain_leek_id = r.json()['opponents'][0]['id']
    print(vilain_leek_id)
    r = requests.get("https://leekwars.com/api/garden/start-solo-fight/" + str(bout_vert) + "/" + str(vilain_leek_id),headers=header)
    # print(r.json())