import json
import requests
import os

PathCredential = "credential.txt"
source_api_adress = "https://leekwars.com/api/"
leek_id = '49273'


###########################
####retrieve passwd from a file, type= id/password
###########################


def readCredential(PathCredential_function, type):
    with open(PathCredential_function) as f:
        data = json.load(f)
    return data[type]


###assign id and password
id_leekwars_global = readCredential(PathCredential, "id")
password_leekwars_global = readCredential(PathCredential, "password")


def UseApi(api_address,api_token):
    if api_token is None:
        response = requests.get(api_address)
    else:
        headers = {'Content-Type': 'application/json',
               'Authorization': 'Bearer {0}'.format(api_token)}
        response = requests.get(api_address,headers)
    if response.status_code == 200:
        # print(str(response.content))
        return json.loads(response.content.decode('utf-8'))
    else:
        return None


###retrieve token from api
def TokenLeekwars(id_leek, passwd_leek):
    if os.path.isfile('./token.txt') == "True":
        file_token = open("token.txt", "r")
        return file_token
    else:
        data_out_TokenLeekwars = UseApi(source_api_adress + "farmer/login-token/" + id_leekwars_global + "/" + password_leekwars_global,None)
        token = data_out_TokenLeekwars['token']
        with open('token.txt', 'w') as file:
            file.write(token)
        return token


def revokeTokenLeekwars(token):
    data_out_revoke = UseApi(source_api_adress + "farmer/disconnect/" + token)
    os.remove("token.txt")
    return data_out_revoke


# def GetOurLeeksId(token):
#     ##difficult because he have to find index of leek
#     return None


def GetGardenForLeek(leek_id, token):
    data_out_GetGardenForLeek = UseApi(source_api_adress + "garden/get-leek-opponents/" + leek_id,token)
    return data_out_GetGardenForLeek


print(GetGardenForLeek(leek_id,TokenLeekwars(id_leekwars_global,password_leekwars_global)))
