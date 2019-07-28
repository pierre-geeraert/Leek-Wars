import json
import requests

PathCredential="credential.txt"
source_api_adress="https://leekwars.com/api/"

###########################
####retrieve passwd from a file, type= id/password
###########################


def readCredential(PathCredential_function,type):
  with open(PathCredential_function) as f:
    data = json.load(f)
  return data[type]

###assign id and password
id_leekwars = readCredential(PathCredential, "id")
password_leekwars = readCredential(PathCredential, "password")

def UseApi(api_address):
    response = requests.get(api_address)
    if response.status_code == 200:
        #print(str(response.content))
        return json.loads(response.content.decode('utf-8'))
    else:
        return None


###retrieve token from api
def TokenLeekwars(id_leek,passwd_leek):
    token = UseApi(source_api_adress + "farmer/login-token/" + id_leekwars + "/" + password_leekwars)
    return token['token']




























#api_url_base = 'https://leekwars.com/api/farmer/login-token/login/passwd'

#headers = {'Content-Type': 'application/json',
    #       'Authorization': 'Bearer {0}'.format(api_token)}

#
# def get_account_info():
#
#     api_url = '{0}account'.format(api_url_base)
#
#     #response = requests.get(api_url, headers=headers)
#     response = requests.get(api_url_base)
#     if response.status_code == 200:
#         print(str(response.content))
#         print("yes")
#
#         with open('person.txt', 'w') as json_file:
#             json.dump(response.content, json_file)
#
#         return json.loads(response.content.decode('utf-8'))
#     else:
#         print("no")
#         return None
# get_account_info()