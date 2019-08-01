from random import randint
import globalVar
from pipenv.utils import requests
from function_essential import readCredential,TokenLeekwars,revokeTokenLeekwars,source_api_address,writeInFile,request_api
from garden import getGardenForLeek,getSoloChallenge,getLeekOpponents,getAI,baddestOpponents,theBaddestOpponents
from fight import makeFight




print(makeFight(globalVar.leek_id,theBaddestOpponents()['id']))
