from random import randint
import globalVar
from pipenv.utils import requests
from function_essential import readCredential,TokenLeekwars,revokeTokenLeekwars,source_api_address,writeInFile,request_api
from garden import getGardenForLeek,getSoloChallenge,getLeekOpponents,getAI,baddestOpponents,theBaddestOpponents
from fight import makeFight,nbrFightAvailable


#print(makeFight(globalVar.leek_id,theBaddestOpponents()['id']))
"""
print(request_api(source_api_address+"ai/get-farmer-ais"))
print(request_api(source_api_address+"ai/save/23456754323456786543/code"))"""

print(request_api(source_api_address+"garden/get")['garden']['fights'])
print(nbrFightAvailable())