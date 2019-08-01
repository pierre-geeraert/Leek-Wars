import json
import time
import os
import requests
import globalVar
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
        token = data_out_TokenLeekwars.json()['token']
        #with open('token.txt', 'w') as file:
        #    file.write(token)
        writeInFile('token.txt',token)
        return token


def revokeTokenLeekwars(token):
    data_out_revoke = request_api(source_api_address + "farmer/disconnect/" + token, None)
    os.remove("token.txt")
    return data_out_revoke


def request_api(address_api):
    try:
        data_out_request_api = requests.get(address_api, headers=globalVar.header)
    except:
        print("request impossible for request_api")
    return json.loads(data_out_request_api.content.decode('utf-8'))


# def getTimeExecution(function):
#     time_begin=time.time()
#     data_out_getTimeExecution=function
#     time_end=time.time()
#     execution_time=time_end-time_begin
#     print(data_out_getTimeExecution)
#     print('{:f}'.format(execution_time))
#     print("execution_time = "+str(execution_time)+" seconds")
#     return execution_time