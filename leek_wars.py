import json
import requests

api_url_base = 'https://leekwars.com/api/farmer/login-token/login/passwd'

#headers = {'Content-Type': 'application/json',
    #       'Authorization': 'Bearer {0}'.format(api_token)}


def get_account_info():

    api_url = '{0}account'.format(api_url_base)

    #response = requests.get(api_url, headers=headers)
    response = requests.get(api_url_base)
    if response.status_code == 200:
        print(str(response.content))
        print("yes")

        with open('person.txt', 'w') as json_file:
            json.dump(response.content, json_file)

        return json.loads(response.content.decode('utf-8'))
    else:
        print("no")
        return None
get_account_info()