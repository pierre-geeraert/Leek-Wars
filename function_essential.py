import json
import os
import requests
from random import randint


source_api_address = "https://leekwars.com/api/"


def readCredential(PathCredential_function, type):
    with open(PathCredential_function) as f:
        data = json.load(f)
    return data[type]


def writeInFile(path_file,data):
    with open(path_file, 'w') as file:
        file.write(data)

def TokenLeekwars(id_leek, passwd_leek):
    if os.path.isfile('./token.txt') == "True":
        file_token = open("token.txt", "r")
        return file_token
    else:
        data_out_TokenLeekwars = requests.post("https://leekwars.com/api/farmer/login-token", data={'login': id_leek, 'password': passwd_leek})
#        token = r.json()['token']
        token = data_out_TokenLeekwars.json()['token']
        #with open('token.txt', 'w') as file:
        #    file.write(token)
        writeInFile('token.txt',token)
        return token


def revokeTokenLeekwars(token):
    data_out_revoke = request_api(source_api_address + "farmer/disconnect/" + token, None)
    os.remove("token.txt")
    return data_out_revoke


def request_api(address_api,token):
    data_out_request_api = requests.get(address_api,headers={'Content-Type': 'application/json','Authorization': 'Bearer {}'.format(token),"Cookie": "PHPSESSID=" + str(randint(0, 1000))})
    return json.loads(data_out_request_api.content.decode('utf-8'))
